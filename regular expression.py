#regular expression is a sequence of characters that forms a search pattern also known as regex or regexp and is used for string matching and manipulation



# import re
# pattern = input("Enter the pattern you want to search:")
# text ="This is a simple text with an expression inside."
# match = re.search(pattern,text)
# if match :
#     print("Match found:",match.group())
# else:
#     print("No match found")



#new and comploex examplew of searching pattern 


import re
pattern = r"[A-Z]+ailway"
text ="he Stockton and Darlington Railway (S&DR), the world's first public railway to use steam locomotives, first operated on 27 September 1825. It initially connected collieries near Shildon with Darlington and Stockton in County Durham, north-east England. The transport of coal proved profitable, and the line was soon extended to a new port at Middlesbrough. The opening of the S&DR was seen as proof of steam railway effectiveness. While coal was hauled by steam locomotives, horses drew passenger coaches along the rails until carriages hauled by locomotives were introduced in 1833. The S&DR suffered severe financial difficulties at the end of the 1840s but the discovery of iron ore in Cleveland led to an increase in revenue. At the beginning of the 1860s it took over railways that had crossed the Pennines, but was itself taken over by the North Eastern Railway, continuing to operate independently until 1876."
match = re.search(pattern,text)
if match :
    print("Match found:",match.group())
else:
    print("No match found")

#example of finding all the matches in a string

import re
pattern = r"[A-Z]+ailway"
text ="he Stockton and Darlington Railway , Tailway,Jailway,pailway (S&DR), the world's first public railway to use steam locomotives, first operated on 27 September 1825. It initially connected collieries near Shildon with Darlington and Stockton in County Durham, north-east England. The transport of coal proved profitable, and the line was soon extended to a new port at Middlesbrough. The opening of the S&DR was seen as proof of steam railway effectiveness. While coal was hauled by steam locomotives, horses drew passenger coaches along the rails until carriages hauled by locomotives were introduced in 1833. The S&DR suffered severe financial difficulties at the end of the 1840s but the discovery of iron ore in Cleveland led to an increase in revenue. At the beginning of the 1860s it took over railways that had crossed the Pennines, but was itself taken over by the North Eastern Railway, continuing to operate independently until 1876."
matches = re.finditer(pattern,text)
for match in matches:
    print("Match found in 2:",match.group())
else:
    print("No match found")


#span method
import re
pattern = r"[A-Z]+ailway"
text ="he Stockton and Darlington Railway , Tailway,Jailway,pailway (S&DR), the world's first public railway to use steam locomotives, first operated on 27 September 1825. It initially connected collieries near Shildon with Darlington and Stockton in County Durham, north-east England. The transport of coal proved profitable, and the line was soon extended to a new port at Middlesbrough. The opening of the S&DR was seen as proof of steam railway effectiveness. While coal was hauled by steam locomotives, horses drew passenger coaches along the rails until carriages hauled by locomotives were introduced in 1833. The S&DR suffered severe financial difficulties at the end of the 1840s but the discovery of iron ore in Cleveland led to an increase in revenue. At the beginning of the 1860s it took over railways that had crossed the Pennines, but was itself taken over by the North Eastern Railway, continuing to operate independently until 1876."
matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])

#FINDALL METHOD
import re
pattern = r"[A-Z]+ailway"
text ="he Stockton and Darlington Railway , Tailway,Jailway,pailway (S&DR), the world's first public railway to use steam locomotives, first operated on 27 September 1825. It initially connected collieries near Shildon with Darlington and Stockton in County Durham, north-east England. The transport of coal proved profitable, and the line was soon extended to a new port at Middlesbrough. The opening of the S&DR was seen as proof of steam railway effectiveness. While coal was hauled by steam locomotives, horses drew passenger coaches along the rails until carriages hauled by locomotives were introduced in 1833. The S&DR suffered severe financial difficulties at the end of the 1840s but the discovery of iron ore in Cleveland led to an increase in revenue. At the beginning of the 1860s it took over railways that had crossed the Pennines, but was itself taken over by the North Eastern Railway, continuing to operate independently until 1876."
matches = re.findall(pattern,text)
for match in matches:
    print("Match found in 4:",match)            


#replace method
import re
pattern = r"[a-z]+at"
text ="The cat sat on the mat and ate a fat rat."
new_text= re.sub(pattern,"dog",text)
print(new_text)   