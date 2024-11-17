# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:19:41 2024

@author: HP 840 g4
"""

class Customer:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = []
        self.orders = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart_items(self):
        return self.cart

    def place_order(self):
        if self.cart:
            self.orders=self.cart[0]
            self.cart=[]
            return "Order placed successfully!"
        else:
            return "Cart is empty. Cannot place an order."
    
    def view_orders(self):
        return self.orders


        
        
        