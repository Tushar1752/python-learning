list1=[1,2,3,4,5,]
list2=["red",'green',"yellow"]
print(list1)
print(list2)


#index printing

list1=[1,2,3,4,5,]
print(list1)
print(list1[0])


#index printing

ist1=[1,2,3,4,5,]
list2=["red",'green',"yellow"]
print(list1)
print(list2)


print(list1[2])
print(list2[0])


#negstive indexing

list1=[2,3,4,5,6]
print(list1[-3])
print(list1[len(list1)-3])

#check wether an element. is in list or not

colors= ["red","yellow","green","white"]
if "yellow" in colors:
     print("yellow is in colour")
else :
     print("yellow is not in list")


# setting range in index

list1=[1,2,3,4,5,6,7,8,9]
print(list1[3:5])
print(list1[-7:-2])


#index jumping

list1=[1,2,3,4,5,6,7,8,9]
print(list1[0:8:2])


#List comprehension

#*accept item with small letter "o"in new list
names = ["milo", "sarah", "Bruno", "Rosa"]
nameWith_O = [item for item in names if "o" in item]
print(nameWith_O)


#*accept item with more than four letter

ames = ["milo", "sarah", "Bruno", "Rosa"]
nameWith_O = [ item for item in names if (len(item)>=4)]
print(nameWith_O)


#new quesrtion


list = [i*i for i in range (4)]
print(list)

ist = [i*i for i in range (4) if i%2==0]
print(list)