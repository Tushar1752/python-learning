i=int(input("enter a number:"))
print("enter number :",i)
for i in range (i):
    print(i,end=' ')
    if(i==50):
        print(" is not allowed")
        break
    else:
        print("missinipi")
print("thank for using this program")




#next program

for i in range(11):
     print("5 X",i+1,"=",5 * (i+1)) 
     if(i==10):
      break
     


#contiue.  kaa

i=int(input("enter a number:"))
print("enter number :",i)
for i in range (i):
    print(i,end=' ')
    if(i==50):
        print(" is not allowed")
        continue
    else:
        print("missinipi")
print("thank for using this program")



#new program

for i in [2,4,6,77,8,0,43]:
    if(i%2==0):
         continue
    print(i)


#next program


i=int(input("enter a number:"))
print("Entrr the number :",i)
while True:
    print(i)
    i=i+1
    if(i>=1000):
        break
    if i%100==0:
        i +=1
        continue