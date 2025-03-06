def is_prime(num):
    """
    This function is used to check the number is prime or not
    Args:
        num: (int) number to check
    Return:
        bool: True if number is prime else False
    """
    result =True
    for index in range(2,num):
        if num%index==0:
            result = False
            break
    return result
def is_factor(num,index):
    """
    This function is used to check the index is factor of number
    Args:
        num: (int) number to check
        index: (int) index to check
    Return:
        bool: True if index is factor of number else False
    """
    return num%index==0
def is_factor(num):
    """
    This function is used to check the number is even or not
    Args:
        num: (int) number to check
    Return:
        bool: True if number is even else False
    """
    
