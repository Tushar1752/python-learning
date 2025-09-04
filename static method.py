class Math:
    @staticmethod
    def add(a,b):
        return a+b
result=Math.add(9,3)
print(result)


#next questtion:

class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return(a+b)
result=Math.add(3,4)
print(result)
a=math(5)
print(a.num)
a.addtonum(7)
print(a.num)