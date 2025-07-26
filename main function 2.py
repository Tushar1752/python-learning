def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)


def isGreater(a,b):
   if(a>b):
      print("first is greter than second")
   elif(a==b):
         print("first is equal to second")
   else:
     print("second is greater than first")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

isGreater(a,b)
calculateGmean(a,b)

# This script calculates the geometric mean of two numbers a and b.



c=int(input("Enter the value of c:"))
d=int(input("Enter the value of d:"))
isGreater(c,d)
calculateGmean(c,d)
# This script calculates the geometric mean of two numbers c and d.