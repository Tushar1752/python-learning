#union method

num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num3=num1.union(num2)
print(num3)
#thius returns a new set that contains all elements from both num1 and num2.

#update method

num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num3=num1.update(num2)
print(num2)  # num1 is updated in place, so it will now contain the union of both sets
# Note: The update method does not return a new set, it modifies num1 in place.


#intersection method 

num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num3=num1.intersection(num2)
print(num3)
#this returns a new set with elements that are common to both num1 and num2.



#intersection_update method
num1={1,2,3,4,5,6}
num2={4,5,6,7,8,9}
num1.intersection_update(num2)
print(num1)
#this modifies num1 in place to keep only elements that are also in num2.

#symmetric difference method
num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num3=num1.symmetric_difference(num2)
print(num3) 
#this returns a new set with elements in either num1 or num2 but not in both.


#symmetric_differnce_update method
num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num2.symmetric_difference_update(num1)
print(num1)
#this modifies num1 in place to keep only elements that are in either num1 or num2 but not in both.

#difference method
num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num3=num1.difference(num2)
print(num3)
#this returns a new set with elements in num1 that are not in num2.


#difference_update method
num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
num2.difference_update(num1)
print(num1)
#this modifies num1 in place to keep only elements that are in num1 but not in num2.

#isdisjoint method
num1={4,5,6,7,8,9}
num2={1,2,3,4,5,6}
print(num1.isdisjoint(num2))
#this returns True if num1 and num2 have no elements in common, otherwise False.    


#issuperset method
#issubset method 

num1={4,5,6,7,8,9}
num2={4,5,6}
print(num1.issuperset(num2))
print(num2.issubset(num1))
#this returns True if num1 contains all elements of num2, otherwise False.  
#issubset method checks if num2 is a subset of num1, meaning all elements of num2 are in num1.


#add and update methods
num1={2,3,4,45,56,6}
num2={1,2,3,4,5,6}
num1.add(100)
print(num1)
num1.update(num2)
#this adds all elements of num2 to num1, modifying num1 in place.)
print(num1)
#add method adds a single element to the set, while update method can add multiple elements from
#an iterable (like a list or another set). Both methods modify the set in place.    


#remove and discard methods
num1={2,3,4,45,56,6}
num1.remove(3)
print(num1)
#this removes the element 3 from num1, raising a KeyError if 3 is

#pop method
num1={2,3,4,56,45,4}
num = num1.pop()
print(num)
print(num1)


#del and clear methods
num1={2,3,4,56,45,4}
del num1
#this deletes the entire set num1, making it undefined.
num={2,3,4,56,45,4}
num.clear()
print(num)
#this removes all elements from the set num, leaving it empty but still defined.
#clear method empties the set, while del removes the set entirely.


#checking if an element exists in a set
num1={2,3,4,56,45,4}
if 3 in num1:
    print("3 is present in the set")
else:
    print("3 nahi hai bhai set mein")
#this checks if the element 3 is present in num1, printing a message accordingly.   
