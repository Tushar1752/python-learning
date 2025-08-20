#Enumerate functioin in python
#This function is used to iterate over a list and get the index of each item

fruits=['banana','apple','orange','kiwi']
for index,fruit in enumerate(fruits):
    print(f"Index: {index},Fruits:{fruit}")


#next question

marks=[89,80,45,22,67]
for index,mark in enumerate(marks):
    print(mark)
    if (index==0):
        print("Awesome")



#changing the start index

fruits=['banana','apple','orange','kiwi']
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
   