# #Calculator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a//b
# e=int(input("Enter the No of time you want to run this operation"))
# for f in range(0,e):
#   x=input("1. add 2 .sub 3. mul 4. div")  
#   c=int(input("Enter the no"))
#   d=int(input("Enter the no"))
#   if x=='1':
#       print(add(c,d))
#   elif x=='2':
#       print(sub(c,d))
#   elif x=='3':
#       print(mul(c,d))
#   else:
#       print(div(c,d))


#this is better and easier to understand rather than making so many functions
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
