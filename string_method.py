str="a,b,c,d,e,f,g,h,i,j,k"
print(str.upper())

#lower 
str="A,B,C,D,E,F,GH,H,I,J,K,L"
print(str.lower())

#strip

str="  white space.   "
print(str.strip())

#rstrip

str="hello !!!"
print(str.rstrip("!"))

#replace

str=("Silver Spoon")
print(str.replace("Sp" , "M"))

#split

str= "Silver Spoon"
print(str.split(" "))

#Capitalize 

str= "Hello"
print(str.capitalize())

str2="hello world"
print(str2.capitalize())

#centre

str=" welcome to console !!!"
print(str.center(30, "."))

#count
str="wali mohammmad bin tuglaq kya hal hai \n bhaijaan "
print(str)
print(str.count("m"))

#endswith #startswith
str = "hello weorld"
print(str.startswith("e"))

#find

str="he is a boy" 
print(str.find("boy"))


#index
str="he is a boy" 
print(str.index("boy"))

#isalnum

str="he is a boy" 
print(str.isalnum())

#isalpha

str="hello"
print(str.isalpha())

#islower 

str='hello world' 
print(str.islower())


#isprintable 

str=("hello beta")
print(str.isprintable())


#isspace


str=" "
print(str.isspace())


#istitle

str="World Health org"

print(str.istitle())

#issupper

str= "HELLO WORLD"
print(str.isupper())

#swapcase

str= "he is a boy"
print(str.swapcase())

#Title

str="comple analysis with integrsal trasnform"
print(str.title())
