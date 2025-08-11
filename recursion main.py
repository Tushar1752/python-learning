def factorial (num):
    if (num==1 or num==0):
        return 1
    else:
        return(num* factorial(num-1))
num = 9;
print("Number :",num)
print("factorial:",factorial(num))





#fabonacci series 


def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
n=9;
print("Fibonacci series:",n)
print("Fibonacci number",fibonacci(n))