# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 06:31:09 2024

@author: HP 840 g4
"""
from Order_management.user_class import User
from Order_management.customer_class import Customer
from Order_management.admin_class import Admin
from Order_management.vendor_class import Vendor
from Order_management.product_class import Product
from Order_management.order_class import Order

def main():
    print("Welcome to the Order Management System")
    print("1. Register as a User")
    print("2. Login as a User")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        role = input("Enter your role (customer/admin/vendor): ")
        user = User(username, email, role)
        print("User registered successfully!")
        print("--------------------------------")
        print("your details are in below:\n--------------------------------\n",user.get_details())

    elif choice == "2":
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        role = input("Enter your role (customer/admin/vendor): ")

        if role == "customer":
            customer = Customer(username, email)
            print("Welcome ",username,"!")
            while True:
                print("\n1. Add product to cart")
                print("2. View cart")
                print("3. Place order")
                print("4. View orders")
                print("5. Exit")
                option = input("Choose an option: ")

                if option == "1":
                    product_name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    product = Product(product_name, price)
                    customer.add_to_cart([product.product_id,product.product_name, product.price])
                    print("Product added to cart.")

                elif option == "2":
                    print("Cart:", *customer.view_cart_items())

                elif option == "3":
                    customer.place_order()
                    print(f"Order ID: {customer.orders[0]}, \nOrder Name:{customer.orders[1]} \nTotal: {customer.orders[2]}")

                elif option == "4":
                    print("Orders:", customer.view_orders())
                elif option=="5":
                    print("Thank you for your time. Goodbye!")
                    break
                else:
                    print("Invalid option.")
            
        elif role == "admin":
            admin = Admin(username, email)
            print("Welcome ",username,"!")
            while True:
                print("\n1. Manage users")
                print("2. Manage products")
                print("3. Exit")
                option = input("Choose an option: ")

                if option == "1":
                    action = input("Enter action (add/remove/update): ")
                    if action=="add" or action=="remove" or action=="update":
                        user_to_manage = input("Enter username to manage: ")
                        admin.manage_users(action, user_to_manage)
                        print("User list:", admin.user_list)
                    else:
                        print("invalid option")

                elif option == "2":
                    action = input("Enter action (add/remove): ")
                    if action=="add" or action=="remove":
                        product_name = input("Enter product name: ")
                        product_price = float(input("Enter product price: "))
                        product = Product(product_name, product_price)
                        admin.manage_products(action, product)
                        print(product.get_details())
                    else:
                        print("invalid option")

                elif option == "3":
                    print("Thank you for your time. Goodbye!")
                    break
                else:
                    print("Invalid option.")

        elif role == "vendor":
            vendor = Vendor(username, email)
            print("Welcome ",username,"!")
            while True:
                print("\n1. Add product")
                print("2. Remove product")
                print("3. View products")
                print("4. Exit")
                option = input("Choose an option: ")

                if option == "1":
                    product_name = input("Enter product name: ")
                    product_price = float(input("Enter product price: "))
                    product = Product(product_name, product_price)
                    vendor.add_product(product)
                    print("Product added.")

                elif option == "2":
                    product_name = input("Enter product name to remove: ")
                    product = next((p for p in vendor.products if p.product_name == product_name), None)
                    if product:
                        vendor.remove_product(product)
                        print("Product removed.")
                    else:
                        print("Product not found.")

                elif option == "3":
                    product=Product(product_name, product_price)
                    print(product.get_details())

                elif option == "4":
                    print("Thank you for your time. Goodbye!")
                    break
                else:
                    print("Invalid option.")
        else:
            print("Invalid role. Please choose customer, admin, or vendor.")

    elif choice == "3":
        print("Exiting the system. Goodbye!")
    else:
        print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

        