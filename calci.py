def add(a,b):
    return a+b;
def subtract(a,b):
    return a-b;
def multiplication(a,b):
    return a*b;
def division(a,b):
    if a==0:
       return "error! division by zero."
    return x/y
def calci():
 print("Select operation:")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. division")
wish = input("enter wish(a/b/c/d):")
num1 = float(input("Enter a no: "))
num2 = float(input("Enter b no: "))
num3 = float(input("Enter c no: "))
num4 = float(input("Enter d no: "))

if wish == 'a':
    print("Result:", add(num1, num2))
elif wish == 'b':
    print("Result:", subtract(num1, num2))
elif wish == 'c':
    print("Result:", multiplication(num1, num2))
elif wish == 'd':
    print("Result:", division(num1, num2))
else:
    print("Invalid input");


