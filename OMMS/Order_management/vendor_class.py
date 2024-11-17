# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:19:01 2024

@author: HP 840 g4
"""

class Vendor:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.products = ["laptop"]

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def view_products(self):
        return self.products


