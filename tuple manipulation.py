#manipulating tuples

countries = ("Spain","Italy","India","England.","Germamy")

temp=list(countries)

print(countries)
temp.append("Russia")
print(temp)
temp.pop(3)
print(temp)
temp[2]="Finland"

print(temp)
countries = tuple(temp)

print(countries)
  

#manipulating tuple without converting themn into list. 

countries = ("Afghanistan","china","Bangladesh","Nepal")
countries2=("India","bhutan","myannmar")

middleeastasia=countries+countries2
print(middleeastasia)