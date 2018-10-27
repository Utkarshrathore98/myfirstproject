#Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
e=int(input("Enter the time you want to do this operation"))
for f in range(0,e):
  x=input("1. add 2 .sub 3. mul 4. div")  
  c=int(input("Enter the no"))
  d=int(input("Enter the no"))
  if x=='1':
      print(add(c,d))
  elif x=='2':
      sub(c,d)
  elif x=='3':
      mul(c,d)
  else:
      div(c,d)
  
