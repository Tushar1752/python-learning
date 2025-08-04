#example for f streing

letter = "My name is {} and i am from {}"
name = "Tushar"
country= "India"
print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}")



# NEXT

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))


#next

letter = "My name is {} and i am from {}"
name=input("Enter the name:")
print("The name is:",name)
country=input("Enter the name of country:")
print("The name of country i:",country)
print(letter.format(name,country))


#fnew question

val='Geeks'
print(f"{val} for {val} is a portal for {val}")
name = 'Tushar'
age = 23
print(f"Hello myself {name} and I am {age} year old")