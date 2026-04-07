inputstr=input("Enter a value: ")
count=0
while inputstr != "":
    neg=int(inputstr)
    if neg < 0:
        count=count+1
    inputstr=input("Enter a value: ")
print(count, "times")
    