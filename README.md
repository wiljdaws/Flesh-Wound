# Endpoint Spider

This Scrapy spider, named "endpoint-spider," is designed to crawl and scrape links.

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

2. Run the spider using the following command:

   ```bash
   scrapy runspider endpoint.py -a base=wikipedia
   ```

   Replace `wikipedia` with your desired base name. If no base is provided, the default is `finance.yahoo`.

### Spider Behavior

- The spider starts by visiting the default specified Wikipedia page (`https://www.wikipedia.com`) or the specified base page (default is `https://www.finance.yahoo.com`) and extracts links from the page.
- It saves unique links to a file named `endpoints.txt` within a directory named after the specified base.
- The spider follows internal links on the page to other pages, recursively collecting links.
- It also looks for tables on the page using CSS selectors (`table` and `div.data-table`) and extracts tabular data.
- Extracted tabular data is printed in dictionary format.

### File Structure

- The spider creates a directory named after the specified base if it doesn't exist.
- Inside this directory, it saves the unique links to a file named `endpoints.txt`.

### Endpoint Spider in Action

![Spider in Action](https://github.com/wiljdaws/scrapy/assets/98637668/3fd9e8cc-22f1-4fbd-beb4-0f910f71cac0)

## Author

- Author: Dawson J. Williams
- Contact: wiljdaws@amazon.com
- LinkedIn: [Dawson J. Williams on LinkedIn](https://www.linkedin.com/in/djwsoftdev/)

Feel free to modify and customize the spider according to your needs.
