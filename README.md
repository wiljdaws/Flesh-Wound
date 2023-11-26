# Endpoint Spider

This Scrapy spider, named "endpoint-spider," is designed to crawl and scrape links

## How to Use

### Prerequisites

Before using the spider, make sure you have Python, Scrapy, and other dependencies installed. You can install them using the following:

```bash
pip install scrapy
```

### Cloning the Repo

```bash
scrapy runspider endpoint.py
```

### Running the Spider

1. Navigate to the scrapy directory.

   ```bash
   cd scrapy/scrapy
   ```
   ![jim](https://github.com/wiljdaws/scrapy/assets/98637668/a73320a1-daa5-4790-a067-3d52b6f2f650)
   
2. Run the spider using the following command:

   ```bash
   scrapy runspider endpoint.py
   ```
   ![zack](https://github.com/wiljdaws/scrapy/assets/98637668/05e5f0c6-2116-4f50-8c63-083f1f0a848c)
### Spider Behavior

- The spider starts by visiting the default specified Wikipedia page (`https://www.wikipedia.com`) and extracts links from the page.
- It saves unique links to a file named `endpoints.txt` within a directory named 'wikipedia.'
- The spider follows internal links on the page to other Wikipedia pages, recursively collecting links.
- It also looks for tables on the page using CSS selectors (`table` and `div.data-table`) and extracts tabular data.
- Extracted tabular data is printed in dictionary format.

### File Structure

- The spider creates a directory named 'wikipedia' if it doesn't exist.
- Inside this directory,

 it saves the unique links to a file named `endpoints.txt`.

### Endpoint Spider in Action

https://github.com/wiljdaws/scrapy/assets/98637668/3fd9e8cc-22f1-4fbd-beb4-0f910f71cac0



## Author

- Author: Dawson J. Williams
- Contact: wiljdaws@amazon.com
- LinkedIn: https://www.linkedin.com/in/djwsoftdev/

Feel free to modify and customize the spider according to your needs. 
