import scrapy
import os

class EndpointSpider(scrapy.Spider):
    name = 'endpoint-spider'
    base = 'wikipedia'
    start_urls = [f'https://www.{base}.com']

    def __init__(self, *args, **kwargs):
        super(EndpointSpider, self).__init__(*args, **kwargs)
        self.visited_links = set()
        self.links_file = os.path.join(self.base, 'endpoints.txt')

    def save_link_to_file(self, link:str)-> None:
        '''
        Save the link to the file
        
        ---
        - Args
            - link (str)
        - Returns
            - None
        '''
        with open(self.links_file, 'a') as f:
            f.write(link + '\n')

    def start_requests(self):
        '''
        Start the spider
        
        ---
        - Args
            - None
        - Returns
            - None
        '''
        if not os.path.exists(self.base):
            os.mkdir(self.base)
        if not os.path.exists(self.links_file):
            open(self.links_file, 'w').close()

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        '''
        Parse the response
        
        ---
        - Args
            - response: scrapy.Response
        - Returns
            - None
        '''
        links = response.css('a::attr(href)').getall()

        for link in links:
            if link not in self.visited_links:
                self.visited_links.add(link)
                self.save_link_to_file(link)

            if link.startswith('http://') or link.startswith('https://'):
                if f'{self.base}' in link:
                    yield response.follow(link, self.parse)

        TABLE_SELECTORS = ['table', 'div.data-table']

        for selector in TABLE_SELECTORS:
            tables = response.css(selector)
            for table in tables:
                for row in table.css('tr'):
                    data = {}
                    for index, cell in enumerate(row.css('td, th')):
                        header = cell.css('th::text').get()
                        key = header if header else f'column{index + 1}'
                        value = cell.css('td::text').get()
                        data[key] = value
                    yield data
