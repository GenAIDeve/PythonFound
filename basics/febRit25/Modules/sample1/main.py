"""This module explain import of function from other modules
   #main .py is executable file
  # utils.py is library file/ logic code you wrie in this file
"""
#import utils// frist i called like this ,here we are importing the utils.py file if i want to just import the is_prime function then i will write from utils import is_prime 
# then i will call just prime function
from utils import is_prime # here i am importing the is_prime function from utils.py file only primenum not evrything from utils.py file
 
num=int(input("Enter the number: "))
#if utils.is_prime(num):  //first i called like this,is_prime is function from utils.py 
if is_prime(num): # here i am calling the is_prime function from utils.py file
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")




#------------------------------------------------------------------\
# dunder
#execute this code when main is used as execution module 'python" main.py'
# this is used to check the code is running from main file 
# generally ppl define the main to start the code from here
if__name__=="__main__"
def main(): #this is entry point we have main function in python
    main() # this is entry point we have main function in python