"""
This modules consist of reusable function
List of function
#is prime
#is factor
"""
def is_prime(num):
    """
    This function checks whether the given number is prime or not
    Args:
    num: int: number to check
    Returns:
    bool: True if number is prime, False otherwise
    """
   
   result = True
   for index in range (2,num):
         if num % index == 0:
              result = False
              break 

