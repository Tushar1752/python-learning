#readlines method

f=open('myfile1.txt','r')
while True:
    line=f.readlines(2)
    if not line:
      break
    print(line)
f.close()

#new mark printing question 
f = open('mynumber1.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    line = line.strip()
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"mark of student {i} in subject English is: {m1}")
    print(f"mark of student {i} in subject SST is: {m2}")
    print(f"mark of student {i} in subject Science is: {m3}")
f.close()

#writelines method

f=open('myfile1.txt','w')
lines=['line\n','line2\n','line3\n']
f.writelines(lines)
f.close()