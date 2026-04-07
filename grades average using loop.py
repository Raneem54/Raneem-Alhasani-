grades= 0
total=0
count=0
while grades >= 0:
    grades= float(input("Enter a graade or -1 to finish: "))
    if grades >= 0:
        total = total+grades
        count= count +1
average=total/count
print(average)