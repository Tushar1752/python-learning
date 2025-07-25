num=int(input("enter a num:"))
print ("the num is :",num)
if(num<0):
     print("the num is negaative")
elif(num>0):
     if(num<=10):
          print("the num is between 1 to 10")
     elif(num>10 and num<=20):
            print("the num is between 11 to 20")
     else :
           print ("the number is greater than 20")
else:
      print("the num is zero")