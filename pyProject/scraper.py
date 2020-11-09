# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urlparse

import os
import pandas as pd
import random
import requests
import time

# Own classes
from book import *

# Owned
__author__ = 'Daniel Laureano Cerviño Cortínez (Danielcc97), Juan Kevin Trujillo (juankevinTR)'
__license__ = '{license}'
__version__ = '1.0.0'
__email__ = 'me@juankevintrujillo.com'

# Code
CSV_PATH = "csv/"


# Function to get last '/' from URL and change it for what we have
# We need to do this cause the page content is not complete
# SOURCE: https://www.geeksforgeeks.org/find-last-index-character-string/
def find_last_index(text, x):
    index = -1
    for i in range(0, len(text)):
        if text[i] == x:
            index = i
    return index


class BooksScraper:
    def __init__(self):
        self.url = "https://books.toscrape.com/"
        self.books = []

    def __get_parsed_html_from_url(self, url):
        return BeautifulSoup(requests.get(url).content, 'html.parser')

    def __get_all_catalogue_links(self, soup):
        catalogue_links = []
        with tqdm(desc="\tGetting catalogue links...") as bar:
            for links in soup.find_all('a'):
                catalogue_links.append(links.get('href'))
                bar.update(1)
        return catalogue_links

    def __get_books_categories_links(self, all_links):
        categories_links = []
        with tqdm(desc="\tGetting books categories links...") as bar:
            for links in all_links:
                if 'catalogue/category/books/' in links:
                    categories_links.append(self.url + links)
                    bar.update(1)
        return categories_links

    def __get_all_links_per_category(self, categories_links):
        links_per_category = categories_links
        with tqdm(desc="\tGetting all links per categories...") as bar:
            for i in links_per_category:
                time.sleep(random.uniform(0, 5))
                soup = self.__get_parsed_html_from_url(i)
                value = find_last_index(i, "/")
                # print("\t\t", i)
                if soup.find('li', class_='next') is not None:
                    links_per_category.append(i[0:value + 1] + soup.find('li', class_='next').find('a').get('href'))
                    bar.update(1)
                else:
                    bar.update(1)
                    continue
        links_per_category.sort()
        return links_per_category

    def __get_all_books_links(self, categories_links):
        books_links = []
        with tqdm(desc="\tGetting all book links...") as bar:
            for link in categories_links:
                time.sleep(random.uniform(0, 5))
                soup = self.__get_parsed_html_from_url(link)
                for text in soup.find_all("div", class_="image_container"):
                    books_links.append(
                        text.find('a').get('href').replace("../../../", self.url + "catalogue/"))
                    bar.update(1)
        return books_links

    def __get_all_books_data(self, books_links):
        books = []
        with tqdm(total=len(books_links), desc="\tGetting all books data...") as bar:
            for i in books_links:
                time.sleep(random.uniform(0, 5))
                soup = self.__get_parsed_html_from_url(i)
                books.append(Book(soup.find('h1').get_text(),
                                  soup.find('img').get('src').replace("../../", self.url),
                                  soup.find('p', class_="star-rating")['class'][1],
                                  soup.find('h2').find_next().get_text(),
                                  soup.find("ul", class_="breadcrumb").find_all('a')[2].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[0].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[1].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[2].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[3].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[4].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[5].get_text(),
                                  soup.find("table", class_="table table-striped").find_all('td')[6].get_text()
                                  ))
                bar.update(1)
        return books

    def __print_waiting(self, text):
        time.sleep(1)
        print("\t\t", text)
        time.sleep(1)

    def __download_images(self, all_books):
        # SOURCE: https://www.kite.com/python/answers/how-to-download-an-image-using-requests-in-python
        with tqdm(total=len(all_books), desc="\tGetting all books images...") as bar:
            for book in all_books:
                time.sleep(random.uniform(0, 5))
                img_data = requests.get(book.image).content
                path = "images/%s" % os.path.basename(urlparse(book.image).path)
                with open(path, 'wb') as handler:
                    handler.write(img_data)
                bar.update(1)

    def __add_header_csv(self, filename):
        df = pd.read_csv(CSV_PATH + filename, delimiter=",",
                         names=["Title", "Image", "Rating", "Description", "Category", "UPC", "Producttype",
                                "Priceextax", "Priceincltax", "Tax", "Availability", "Numberreviews"],
                         header=None)
        df.to_csv(CSV_PATH + filename, sep=',')
        print(df)

    def scrape(self):
        print("\tWeb Scraping of books' data from " + "'" + self.url + "'...")

        # Download HTML
        soup = self.__get_parsed_html_from_url(self.url)

        # Get catalogue links
        catalogue_links = self.__get_all_catalogue_links(soup)
        self.__print_waiting("There are %s catalogue links" % len(catalogue_links))

        # Get books categories links
        books_categories_links = self.__get_books_categories_links(catalogue_links)
        self.__print_waiting("There are %s books categories links" % len(books_categories_links))

        # Get all links per category
        links_per_category = self.__get_all_links_per_category(books_categories_links)
        self.__print_waiting("Categories are divided between %s links" % len(links_per_category))

        # Get all books links
        books_links = self.__get_all_books_links(links_per_category)
        self.__print_waiting("There are %s books" % len(books_links))

        # Get all books data
        all_books = self.__get_all_books_data(books_links)

        # Download Images
        self.__download_images(all_books)

        # Save books in global variable
        self.books = all_books

    def data2csv(self, filename):
        # The file is created if it doesn't exist, and overwrite
        # Dump all the data with CSV format.
        with open(CSV_PATH + filename, "w") as file:
            with tqdm(total=len(self.books), desc="\tCreating dataset...") as bar:
                for book in self.books:
                    file.write(book.get_book_csv_format() + "\n")
                    bar.update(1)
                self.__add_header_csv(filename)
