# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:56:53 2024

@author: HP 840 g4
"""
'''user class'''
class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role

    def get_details(self):
        return f"\nUsername: {self.username}, \nEmail: {self.email}, \nRole: {self.role}"

    def update_email(self, new_email):
        self.email = new_email
        return f"Email updated to {new_email}"



             