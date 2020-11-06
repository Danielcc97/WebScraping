# -*- coding: utf-8 -*-

# Owned
__author__ = 'Juan Kevin Trujillo (juankevinTR)'
__license__ = '{license}'
__version__ = '1.0.0'
__email__ = 'me@juankevintrujillo.com'


# Code
def add_quotation_marks(text):
    return "\"" + text + "\""


class Book:
    def __init__(self, title, image, rating, description, category, UPC, producttype, priceextax, priceincltax, tax,
                 availability, numberreviews):
        self.title = title
        self.image = image
        self.rating = rating
        self.description = description
        self.category = category
        self.UPC = UPC
        self.producttype = producttype
        self.priceextax = priceextax
        self.priceincltax = priceincltax
        self.tax = tax
        self.availability = availability
        self.numberreviews = numberreviews

    def get_book_csv_format(self):
        book_string = ""
        for i in self.__book_to_array():
            book_string = book_string + i + ","
        return book_string[:-1]

    def __book_to_array(self):
        return [add_quotation_marks(self.title),
                add_quotation_marks(self.image),
                add_quotation_marks(self.rating),
                add_quotation_marks(self.description),
                add_quotation_marks(self.category),
                add_quotation_marks(self.UPC),
                add_quotation_marks(self.producttype),
                add_quotation_marks(self.priceextax),
                add_quotation_marks(self.priceincltax),
                add_quotation_marks(self.tax),
                add_quotation_marks(self.availability),
                add_quotation_marks(self.numberreviews)
                ]
