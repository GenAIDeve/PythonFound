

if __name__ == '__main__':
    numbar1 =int(input("Enter the first number1: "))
    numbar2 =int(input("Enter the second number2: "))
    print (numbar1 + numbar2)
except Excaption as e:
    print("Invalid input")
finally:
    print("The program has ended")