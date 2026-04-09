n=int(input("enter the number to show its  multiplication table: "))

def  multiplicationTable(n):
 for i in range(1,13):
    mult=n*i
    print(n,"*",i,"=",mult)
 
print(multiplicationTable(6))