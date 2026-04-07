grade=0
minimum=100
while grade>= 0:
     grade=float(input("Enter a graade or -1 to finish: "))
     if grade <= minimum and grade >=0:
         minimum=grade
print(minimum)