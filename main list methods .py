# list sorting

num=[8,3,2,5,1,6,0,4,9]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

#taking input from user and sort
num=input("E nter the numbers:")
num_list = [int (x ) for x in num.split()]
num_list.sort()
print(num_list)


#index checking

l=[6,3,1,8,0]
print(l.index(3))


#copy method

colors = ["violet","green","indigo"]
print(colors.count("green"))


#copy method

colors = ["violet","green","indigo","blue"]
newlist= colors.copy()
print(colors)
print(newlist)



#new question

l=[3,5,2,53,24,22,1]
print(l)
m=l.copy()
m[0]=4444
print(l)


#inset method 

colors=["red","yellow","Blue","green"]
colors.insert(1,"pink")
print(colors)
