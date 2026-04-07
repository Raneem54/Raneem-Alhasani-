num=input("Enter a value or empty to finish : ")
current=0
while num != "":
    previous=int(num)
    if previous!=current:
     print(previous)
     current=previous
     num=input("Enter a value or empty to finish : ")
    else:
     print("This adjucent to previous input")
     num=input("Enter a value or empty to finish : ")
print(num)
 
 