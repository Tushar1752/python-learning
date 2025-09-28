name=input("Enter the name:")
age=int(input("Enter the age :"))
marks=int(input("Enter the marks:"))
print("My name is",name,"I am ",age,"year old and I scored ",marks,"marks")

if marks>33:
    print("Congrats bro you are passed")
else: 
    print("fail hai tu chutiye")

#next question

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def is_passed(self):
        if self.marks>=40:
            return "pass"
        else:
            return "fail"
        
s1=Student("Tushar",98,85)
s2=Student("Rahul",23,33)
s3=Student("Himesh",45,99)
print(f"Name:{s1.name},Roll_No:{s1.roll_no},Marks:{s1.marks}→ {s1.is_passed()}")
print(f"Name:{s2.name},Roll_no:{s2.roll_no},marks:{s2.marks}→{s2.is_passed()} ")
print(f"Name:{s3.name},Roll_no:{s3.roll_no},marks:{s3.marks}→ {s3.is_passed()}")


#next question


class Animal:
    def speak(self):
        return "Animal Sound"
class Dog(Animal):
    def speak(self):
        return "bark"
a=Animal()
d=Dog()

print(f"Animal says:{a.speak()}")
print(f"Dog says:{d.speak()}")

#next question 

class Animal:
    def speak(self):
        return "Animal Sound"
class Cat(Animal):
    def speak(self):
        return "Meow"
a=Animal()
d=Cat()

print(f"Animal says:{a.speak()}")
print(f"Cat says:{d.speak()}")

#next question

try:
    num=float(input("Enter the number:"))
    reciprocal=1/num
    print("The reciprocal of num is:",reciprocal)
except ZeroDivisionError:
    print("Zero ka division nahi hota")

#greet function

def greet(name):
    print("Good morniung",name)
print("___Starting function____")
greet("Tushar")
print("____Ending function____")


#next questiion

# contacts={}
# while True:
#     name=input("Enter the name (or 'show' to display contacts ,'exit'to quit)")
#     if name.lower()=='exit':
#         break
#     elif name.lower()=='show':
#         for n, p in contacts.items():
#             print(f"Name: {n}, Phone: {p}")
#     else:
#         phone=input("Enter an number")
#         contacts[name]=phone

# close()

#next question of file O/P

with open("number.txt",'r') as f:
  data=f.read()
nums=list(map(int,data.split()))
total=sum(nums)
print("Numbers in file:",nums)
print("Sum of file number:",total)



#next quistion 

with open ("number.txt",'r') as f:
    data=f.read()
words=data.split()
print("The total word inside the txt file is",len(words))



#next questrion

