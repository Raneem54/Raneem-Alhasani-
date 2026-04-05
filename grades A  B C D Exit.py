grade=float(input("Enter the grade:"))
if grade<0 and grade>100:
    exit("Error")
elif grade>=90:
        print("A")
elif grade>=80:
        print("B")
elif grade>=70:
        print("C")
elif grade>=60:
        print("D")
else:
        print("F")