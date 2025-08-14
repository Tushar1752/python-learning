#Dictionary method

#update() method
info={'name':'Tushar','age':20}
print(info)
info.update({'age':22})
info.update({'DOB': '01/04/2004'})
print(info)


#clear method
info={'name':'Tushar','age':30}
info.clear()
print(info) 
#output will be empty dictionary


#pop method
info={'name':'Tushar','age':20}
info.pop('age')
print(info)
#it will remove the key 'age' and its value from the dictionary

#popitem method
info={'name':'Tushar','age':44}
info.popitem()
print(info)
#it will remove the last inserted key-value pair from the dictionary    


#del method
info={'name':'Tushar','age':20}
del info['name']
print(info)
#it will remove the key 'age' and its value from the dictionary 
