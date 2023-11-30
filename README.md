# Flesh Wound

![fleshwound](https://github.com/wiljdaws/Flesh-Wound/assets/98637668/73aa2571-c56f-49a6-b692-17011daa9826)

## Use Case
This Scrapy spider, named "endpoint-spider," is designed to crawl and scrape links and extract all tables found.

## How to Use

## Prerequisites

Before using the spider, make sure you have Python, Scrapy, and other dependencies installed.

You can install them using the following:

```bash
pip install scrapy
```

## Cloning the Repo

```bash
git clone https://github.com/wiljdaws/Flesh-Wound.git
```

## Running the Spider

1. Navigate to the scrapy directory.

   ```bash
   cd Flesh-Wound/flesh_wound/spiders
   ```

   ---
   
   <div align="center">
     <img src="https://media4.giphy.com/media/fQZX2aoRC1Tqw/giphy.gif?cid=ecf05e47jgva86pyiiyllph7g0li5ey6gjqtdqxnzj103crn&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="bruce alighty typing gif">
   </div>

   ---

3. Run the spider using the following command:

   ```bash
   scrapy runspider endpoint.py -a base=yahoo
   ```

   ---
   
   <div align="center">
      <img src="https://media0.giphy.com/media/3owzW5c1tPq63MPmWk/giphy.gif?cid=ecf05e47k7ubd0lvev4naa1rpubar1ory073zotrubsgoudl&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="calculating gif">
   </div>

   ---

   Replace `wikipedia` with your desired base (website) name.
   - If no base is provided
      - default: `finance.yahoo`

## Spider Behavior

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

## File Structure

- The spider creates a directory named after the specified base if it doesn't exist.
- Inside this directory, it saves the unique links to a file named `endpoints.txt`.

## Endpoint Spider in Action


https://github.com/wiljdaws/Flesh-Wound/assets/98637668/b7b0057b-7cae-4a5e-baee-de6c7afad6f4

---

<div align="center">
  <img src="https://media.tenor.com/Rp5tG0HHS74AAAAC/monty-python-ive-had-worse.gif" alt="Flesh Wound">
</div>

---

## Disclaimer

**Note:** Ensure that your use of this spider complies with all applicable laws and regulations. Respect the terms of service of the websites you are scraping. Unauthorized scraping may violate the terms of service of a website and could lead to legal consequences. Use this spider responsibly and ethically.

**Disclaimer:** The author of this spider is not legally responsible for any misuse, unlawful activities, or violations of terms of service that may occur in the use of this spider. Users are solely responsible for their actions.


## Author

- Author: Dawson J. Williams
- Contact: wiljdaws@amazon.com
- LinkedIn: [Dawson J. Williams on LinkedIn](https://www.linkedin.com/in/djwsoftdev/)

## License
- MIT - https://github.com/wiljdaws/scrapy/blob/main/LICENSE

##### Note: *Feel free to modify and customize the spider according to your needs.*
