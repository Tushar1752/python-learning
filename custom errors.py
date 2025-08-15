#raising custom errors =

#Value Error example

salary=int(input("Enter your salary:"))
if not 2000<salary<5000:
    raise ValueError("Salary must be between 2000 and 5000")

#i want to make a update in this if user give input quit in small letter then it should avoid value error

salary = input("enter the salary :")
if salary.lower() == 'quit':
      print("Existing the program")
else:
     salary=int(salary)
     if not 2000<salary<5000:
          raise ValueError("Salary must be between 2000 and 5000")
     print("salary is valid and accepted:",salary)
    