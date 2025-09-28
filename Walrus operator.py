#Walrus operator is used to assign values to variables as part of a larger expression. and it is represented by := also known as assignment expression.
#It was introduced in Python 3.8.      

#example 1:

numbers = [1,2,3,4,5]
while (n:= len(numbers))>0:
    print(numbers.pop())


#example 2:
names=["Tushar","Deeksha","Rahul"]
if (name:=input("Enter your name:")) in names:
    print(f"Hello,{name}")
else:
    print("Name not found")


#example 3:

happpy=True
print(happy:=True)
print(happy)

#without walrus operator

foods=list()
while True:
    food=input("What food do you like?")
    if food=='quit':
        break 
    foods.append(food)
print(foods)
#with walrus operator

foods=list()
while food:=input("What food do you like?")!='quit':
    foods.append(food)

print("You like the following foods:",foods)