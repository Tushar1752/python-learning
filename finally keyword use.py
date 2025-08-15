#try and except block without finally keyword

try:
  L=[1,2,3,4]
  print(type(L))
  i=int(input("Enter an index:"))
  print(L[i])
except:
      print("Some error occured")



#try and except block with finally keyword
try:
    L=[1,2,3,4]
    print(type(L))
    i=int(input("Enter an index:"))
    print(L[i])
except:
    print("Some error occured")
finally:
    print("end of the progeram")


#new way using def 

def func1():
    try:
        L = [1, 2, 3, 4]
        print(type(L))
        i = int(input("Enter an index: "))
        print(L[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    
x=func1()
print(x)


