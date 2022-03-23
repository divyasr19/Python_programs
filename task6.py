#program for calculator
x=float(input("enter value for x:"))  #accessing value1
y=float(input("enter value for y:"))  #accessing value2
z=input("enter opration for z:") #mention your operation
if z=='+':
    print(x+y)
elif z=='-':
    print(x-y)
elif z=='*':
    print(x*y)
elif z=='/':
    print(x/y)
else:
    print("select a valid operation")