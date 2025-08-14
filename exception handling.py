a=input("Enter the number :")
print("Multiplicatiuom tasble of {a} is:")
try:
  for i in range (1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e :
  print(e)

print(" Some imp lines of code")
print("End of the program")
print("Thank you for using the program")
print("Have a nice day")
print("Goodbye!")
print("Please try again with a valid number in table")

#this code is to demonstrate exception handling in Python
#It will handle the case where the input is not a valid integer
#and will not crash the program, instead it will print an error message
#and continue to execute the rest of the code.



#now i am going to add some more lines of code
a=input("Enter the number :")
print("Multiplicatiuom tasble of {a} is:")
try:
  for i in range (1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e :
  print("An error occured")

print(" Some imp lines of code")
print("End of the program")


#now i am going to give example of value error
try:
    a=int(input("Enter an integer nuumber: "))
except ValueError:
  print("Number enterd is not an integer")
except IndexError:
    print("Index error occured")