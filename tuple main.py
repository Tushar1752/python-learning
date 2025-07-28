tup = (1,)
print(type(tup),tup)

#tuple example 

tup=(4,6,2,1,6,3)
tup2=("apple","mangto","potatol")
print(tup)
print(tup2)

details = ("abhijet ",18,"FYBscIT",9.8)
print(details)



#tuple index 

country = ("spain","italy","india","china")
print(country.index("india"))

#(i)positive indexing
print(country[2])

#(ii)negative indexing

print(country[-2])

#(iii)check for item

if "Germany" in country:
    print("Germany hai bhai")
else:
    print("Germany is absent")


#(iv) range of index

print(country[0:2])


#printing all element from a given index till the end

print(country[1:])
print(country[-3:])


#printing all elemenmt from start to a given index

print(country[:2])
print(country[:-1])