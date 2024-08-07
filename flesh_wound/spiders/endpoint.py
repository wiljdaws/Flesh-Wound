import scrapy
import os
import csv
import logging

class EndpointSpider(scrapy.Spider):
    name = 'endpoint-spider'
    base = 'finance.yahoo'

    def __init__(self, *args, **kwargs):
        super(EndpointSpider, self).__init__(*args, **kwargs)
        self.visited_links = set()
        self.base_dir = self.base
        self.links_file = os.path.join(self.base_dir, 'endpoints.txt')
        self.tables_dir = os.path.join(self.base_dir, 'tables')
        self.logs_dir = os.path.join(self.base_dir, 'logs')
        self.setup_logging()

    def setup_logging(self):
        if not os.path.exists(self.logs_dir):
            os.makedirs(self.logs_dir)

        log_file_path = os.path.join(self.logs_dir, 'spider.log')

        logging.basicConfig(
            filename=log_file_path,
            format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
            level=logging.DEBUG  # Change to logging.ERROR for production
        )

        # Redirect Scrapy's logs to the same logging system
        logging.getLogger('scrapy').setLevel(logging.DEBUG)

    def add_arguments(self, parser):
        parser.add_argument('-b', '--base', default='finance.yahoo', help='Base variable for the spider')

    def start_requests(self):
        os.makedirs(self.base_dir, exist_ok=True)
        open(self.links_file, 'a').close()

        base = getattr(self, 'base', 'finance.yahoo')
        if not base.startswith(('http://', 'https://')):
            base = f'https://www.{base}.com'
        
        self.start_urls = [base]

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        try:
            links = response.css('a::attr(href)').getall()

            for link in links:
                full_link = response.urljoin(link)
                if full_link not in self.visited_links:
                    self.visited_links.add(full_link)
                    self.save_link_to_file(full_link)

                if link.startswith(('http://', 'https://')) and self.base in link:
                    yield response.follow(link, self.parse)

            table_selectors = ['table', 'div.data-table']

            for selector in table_selectors:
                for table in response.css(selector):
                    table_data = self.extract_table_data(table)
                    
                    if table_data:
                        self.save_table_to_csv(table_data)

                    yield table_data

        except Exception as e:
            # Log the error and continue
            logging.error(f"Error processing {response.url}: {str(e)}")

        return None

    def extract_table_data(self, table):
        table_data = []
        headers = table.css('thead th::text').getall()

        if not headers:
            headers = table.css('th::text').getall()
                
        for row in table.css('tbody tr'):
            data = dict.fromkeys(headers, '')
            cells = row.css('td')
            try:
                for index, cell in enumerate(cells):
                    data[headers[index]] = cell.css('::text').get()
            except IndexError:
                continue

            table_data.append(data)

        return table_data

    def save_link_to_file(self, link: str) -> None:
        with open(self.links_file, 'a') as f:
            f.write(link + '\n')

    def save_table_to_csv(self, table_data: list) -> None:
        try:
            if not os.path.exists(self.tables_dir):
                os.makedirs(self.tables_dir)

            csv_file_path = os.path.join(self.tables_dir, f'table_{len(os.listdir(self.tables_dir)) + 1}.csv')

            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=table_data[0].keys())
                writer.writeheader()
                writer.writerows(table_data)

        except Exception as e:
            # Log the error and continue
            logging.error(f"Error saving table to CSV: {str(e)}")

if __name__ == "__main__":
    from scrapy import cmdline
    cmdline.execute("scrapy crawl endpoint-spider".split())
