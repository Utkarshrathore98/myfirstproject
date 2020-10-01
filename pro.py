#Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def mod(a,b):
    return a%b
e=int(input("Enter the No of time you want to run this operation"))
for f in range(0,e):
  x=input("1. add 2 .sub 3. mul 4. div 5. mod")  
  c=int(input("Enter the no"))
  d=int(input("Enter the no"))
  if x=='1':
      print(add(c,d))
  elif x=='2':
      print(sub(c,d))
  elif x=='3':
      print(mul(c,d))
  elif x=='4':
      print(div(c,d))
  elif x=='5':
    print(mod(c,d))
  else:
    print("Invalid Input")
