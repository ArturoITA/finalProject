'''
Created on Mar 7, 2020

@author: ITAUser
'''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("A.Add")
print("S.Subtract")
print("M.Multiply")
print("D.Divide")
 
choice = input("Enter A, S, M, or D for Operation: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 'a' or 'A':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == 's' or 'S':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 'm' or 'M':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 'd' or 'D':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")