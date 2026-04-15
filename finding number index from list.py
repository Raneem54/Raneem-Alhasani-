values=[5,9,6,7,3,10]
index = -1
value=int(input("Enter a value that you want to find: "))
for i in range(len(values)):

    if values[i]==value:
     index = i
     break
print(index)