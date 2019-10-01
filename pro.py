#Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
e=int(eval("Enter the No of time you want to run this operation"))
for f in range(0,e):
  x=input("1. add 2 .sub 3. mul 4. div")  
  c=int(eval("Enter the no"))
  d=int(eval("Enter the no"))
  if x=='1':
      print(add(c,d))
  elif x=='2':
      print(sub(c,d))
  elif x=='3':
      print(mul(c,d))
  else:
      print(div(c,d))
  
