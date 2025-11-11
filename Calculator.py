a = 0
b = 0
diya = ""
a=input("Enter first number:")
b=input("Enter second number:")
diya=input("Enter the operation (+, -, *, /):")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if diya == "+":
    print("The sum is:", add(a, b))

elif diya == "-":
    print("The difference is:", subtract(a, b))

elif diya == "*":
    print("The product is:", multiply(a, b))