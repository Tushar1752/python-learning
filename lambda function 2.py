#without lambda function
def double (x):
   return x*2
print(double(5))

def triple(x):
   return x*x*x
print(triple(3))




#lsmbds function to double the input
double_lambda=lambda x:x*2
cube = lambda x: x*x*x
average=lambda x,y:(x+y)/2

print("average;" ,average(4,6))

print("CUBE",cube(6))

print("DOUBLE_LAMBDA:",double_lambda(5))


#PASING function to functiom

def appl (fx ,value):
   return 6 + fx(value)
print("bekar:", appl(cube,7))
