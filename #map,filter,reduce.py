#map function

numbers=[1,2,3,4,5]
doubled=list(map(lambda x:x*2,numbers))
print(doubled)



#filter
def filter_function(a):
    return a>4


list1=[2,5,6,7,8,9]
new1=filter(filter_function,list1)
print(list(new1))


#Reduce function

from functools import reduce
numbers2=[3,4,5,7,8,9,1]
sum=reduce(lambda x,y:x+y,numbers2)
print(sum)