#Seek() function

with open('myfile1.txt','r') as f :
    #move to 10 th byte in file
    f.seek(10)
    #Read next 5 byte
    data=f.read(5)
    print(data)



#Tell function

with open('myfile1.txt','r') as f:
    data=f.read(10)
    print(f.tell())
    current_position=f.tell()
    f.seek(current_position)
#truncate function

with open('myfile1.txt','w') as f:
  f.write('Hello world!')
  f.truncate(5)
with open('myfile1.txt','r') as f:
  print(f.read())