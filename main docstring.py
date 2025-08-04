#Docstring definition and their example

def square(n):
   ''' Takes in the valuie of a number n, \n return the square  of n'''
   print(n**2)
square(5)



#how to print the docstring we entered

def square(n):
   ''' Takes in the valuie of a number n, \n return the square  of n'''
   print(n**2)
square(5)
print(square.__doc__)


# if we write anything between docstring and function we get error or we get\n value as none


def square(n):
  print(n)
''' Takes in the valuie of a number n, \n return the square  of n'''
   print(n**2)
square(5)
print(square.__doc__)

