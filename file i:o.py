#Opening a file in read mode


f=open('tushar.txt','r')

#reading from a file
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)

#Writing to a file
#To write something to a file we firstly need to open it in write mode
f = open('myfile.txt', 'w')


#We can then use the write() method to write to the file
f=open('myfile.txt','w')
f.write('Hello bhai sahab ')


#Closing a file

f=open("myfile.txt","r")
f.close()



#THE with statement 

with open('myfile.txt','r') as f:
