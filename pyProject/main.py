# -*- coding: utf-8 -*-

import time
from scraper import BooksScraper

# Owned
__author__ = 'Daniel Laureano Cerviño Cortínez (Danielcc97), Juan Kevin Trujillo (juankevinTR)'
__license__ = '{license}'
__version__ = '1.0.0'
__email__ = 'me@juankevintrujillo.com'


# Code
def main():
    output_file = "dataset.csv"

    start_time = time.time()
    print("\n--- Scraping started ---")
    scraper = BooksScraper()
    scraper.scrape()
    scraper.data2csv(output_file)
    scraper.data2dataframe(output_file)
    print("--- Scraping finished in %s minutes ---" % round((time.time() - start_time) / 60, 3))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
