"""This module explain import of function from other modules
   #main .py is executable file
  # utils.py is library file/ logic code you wrie in this file
"""
import utils

num=int(input("Enter the number: "))
if utils.is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")



number = 29 



