# calling factorial and is prime from basic.py and advanced.py
# i have package inside package i have sub package(folder) inside that i have module (some logic codesfiles)
# inside that i have some modules  and from one modules to you are calling another modules
# to execute code in main.py by calling perticular functions 
# eg: just prime number or anycode by classname(utilities.folder.classname import primenumberfunction)  
#The Python Standard Library is a collection of modules and packages that come bundled with Python, providing a wide range of functionality to simplify programming tasks. It eliminates the need to rewrite commonly used code by offering pre-written solutions for various operations. Here are the key features:
#Key Features of the Python Standard Library
#Built-in Modules: Includes modules written in C for system-level functionality (e.g., os for file and directory management, sys for system-specific parameters).
#Extensive Coverage: Offers modules for math operations (math), random number generation (random), string manipulation, data serialization (pickle), and more.
#Portability: Abstracts platform-specific differences into platform-neutral APIs, making Python programs portable across systems.
#Ease of Use: Modules can be imported directly into scripts to access their functionality.
#Commonly Used Modules
#os: Interact with the operating system.
#sys: Access system-specific parameters and functions.
#math: Perform mathematical operations.
#random: Generate random numbers.
#time: Work with time-related functions.
#re: Perform regular expression operations.
#socket: Handle low-level networking.




from utilities.math.advanced import factorial
from utilities.math.basic import is_prime


# main.py


if __name__ == '__main__':  # Correct syntax for this check
    number = int(input("Enter the number: "))  # Get user input
    print(is_prime(number))  # Check if the number is prime
    print(factorial(number))  # Calculate and print the factorial



    
