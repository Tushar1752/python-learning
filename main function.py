def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
if(a>b):
    print("a is greter than b")
else:
    print("b is greater than a")


# This script calculates the geometric mean of two numbers a and b.
calculateGmean(a,b)



c=int(input("Enter the value of c:"))
d=int(input("Enter the value of d:"))
if(c>d):
    print("c is greater than d ")
else:
    print("d is greater than c")

calculateGmean(c,d)
# This script calculates the geometric mean of two numbers c and d.