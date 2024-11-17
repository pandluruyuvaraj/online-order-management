# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:39:23 2024

@author: HP 840 g4
"""

class Order:
    def __init__(self, products, customer):
        self.products = products
        self.customer = customer
        self.order_id = f"ORD{str(id(self))[-5:]}"
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return sum(product['price'] for product in self.products)



        