#program for SI and CI
p=int(input("pricipal:"))#principal amt
t=int(input("time period:"))#time
r=int(input("rate of interest"))#rate of interest
SI=(p*t*r)/100#formula for simple interest
print("simple interest is",SI)#printing

print("compound interest:")
n=int(input("no.of years:"))#no. of years to be calculated
a=p*(1+(r/n))**(t*n)#total amt
CI=a-p#compound interest 
print("compound interest is",CI)