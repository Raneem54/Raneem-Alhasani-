
def Fibonacci(num):
 a=0
 b=1
 print(a," ",end="")
 for i in range(0,num):
    temp=a
    a=b
    b=temp+b
    
    if a<=num:
     print(a," ",end="")
 
Fibonacci(7)
     
     