# Flesh Wound

This Scrapy spider, named "endpoint-spider," is designed to crawl and scrape links and extract all tables found.

## How to Use

### Prerequisites

Before using the spider, make sure you have Python, Scrapy, and other dependencies installed.

You can install them using the following:

```bash
pip install scrapy
```

### Cloning the Repo

```bash
git clone https://github.com/wiljdaws/scrapy.git
```

### Running the Spider

1. Navigate to the scrapy directory.

   ```bash
   cd scrapy/scrapy
   ```
   ![jim](https://github.com/wiljdaws/scrapy/assets/98637668/062d0bb9-3973-43c6-92bc-ef4bc61b4b5f)

2. Run the spider using the following command:

   ```bash
   scrapy runspider endpoint.py -a base=wikipedia
   ```
   ![zack](https://github.com/wiljdaws/scrapy/assets/98637668/c3906339-2207-45b1-81be-1b3b0045652b)

   Replace `wikipedia` with your desired base name.
   - If no base is provided
      - default: `finance.yahoo`

### Spider Behavior

- The spider starts by visiting the default specified page
   - In this case
      - `https://www.wikipedia.com`
   - Or the default base page if none is specified
      - `https://www.finance.yahoo.com`
   - Extracts links and tables from the page.
      - It saves unique links to a file named `endpoints.txt`
         - Saves to a directory named after the specified base (website).
      - The spider follows internal links on the page to other pages
         - Recursively collects links.
      - It also looks for tables on the page
         - Uses CSS selectors
            - `table` and `div.data-table`
            - Extracts tabular data.
      - Extracted tabular data is saved to the tables folder.

### File Structure

- The spider creates a directory named after the specified base if it doesn't exist.
- Inside this directory, it saves the unique links to a file named `endpoints.txt`.

### Endpoint Spider in Action

https://github.com/wiljdaws/scrapy/assets/98637668/2a27351a-4e1a-4a35-bd45-67b3e87d3ca2

### Disclaimer

**Note:** Ensure that your use of this spider complies with all applicable laws and regulations. Respect the terms of service of the websites you are scraping. Unauthorized scraping may violate the terms of service of a website and could lead to legal consequences. Use this spider responsibly and ethically.

**Disclaimer:** The author of this spider is not legally responsible for any misuse, unlawful activities, or violations of terms of service that may occur in the use of this spider. Users are solely responsible for their actions.


## Author

- Author: Dawson J. Williams
- Contact: wiljdaws@amazon.com
- LinkedIn: [Dawson J. Williams on LinkedIn](https://www.linkedin.com/in/djwsoftdev/)

## License
- MIT - https://github.com/wiljdaws/scrapy/blob/main/LICENSE

##### Note: *Feel free to modify and customize the spider according to your needs.*
