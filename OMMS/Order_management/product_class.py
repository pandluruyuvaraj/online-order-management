# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:33:48 2024

@author: HP 840 g4
"""

class Product:
    def __init__(self, product_name, price):
        self.__count=0
        self.product_id=self.__count+1
        self.product_name = product_name
        self.price = price

    def get_details(self):
        return f"product id:{self.product_id} Product: {self.product_name}, Price: {self.price}"

        