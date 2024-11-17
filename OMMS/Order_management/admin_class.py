# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:43:20 2024

@author: HP 840 g4
"""
'''class Admin'''

class Admin:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.user_list = []
        self.product_list = []

    def manage_users(self, action, user):
        if action == 'add':
            print("user is added.")
            self.user_list.append(user)
        elif action == 'remove':
            print("user is removed")
            self.user_list.remove(user)
        elif action == 'update':
            new_name=input("Enter new name:")
            for i in range(len(self.user_list)):
                if self.user_list[i]==user:
                    self.user_list[i]=new_name 
            print("user name is upadted.")                             

    def manage_products(self, action, product):
        if action == 'add':
            self.product_list.append(product)
        elif action == 'remove':
            self.product_list.remove(product)
        elif action == 'update':
            new_product_name=input("Enter new name:")
            for i in range(len(self.product_list)):
                if self.product_list[i]==product:
                    self.product_list[i]=new_product_name
            print("product name is updated.")

