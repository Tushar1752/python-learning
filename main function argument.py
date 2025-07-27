#default argument

def name(fname, mname="jon",lname="watson",):
    print("hello", fname,mname,lname)
name("Any")

#problem 2

def average(a=9,b=2):
    print("the average is:",(a+b)/2)
average(3,9)
#here console will take value from lasst one not from above first given


#required argment 

def average(a,b):
    print("The average of two number is ", (a+b)/2)
average(384848438,888)


#keyword arguments

def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)
name(fname="peter",mname="Weaker",lname="Jada")


#keyword argument 

def name(fname,mname,lname="bhai"):
    print("Hello,",fname,mname,lname)
name("harshit","chor",)

#isme lname default le lega

#length variable argument
#* arbitary length variable aargument

def name(*name):
   print("hello",name[0],name[1],name[2])
name("James","buckman","faster")


#ex=2
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))

average (5,6,8)
  

#*keyword arbitary argument

def name(**name):
   print("Hello,",name["fname"],name["mname"],name["lname"])
name(fname="harshit",mname="badmash",lname="hai")



#return statement

def name (fname,mname,lname):
 return "Hello, " + fname + " " + mname + " " + lname
print(name("james","verma","singh"))