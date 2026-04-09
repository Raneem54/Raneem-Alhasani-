total=0
average=0
while True:
 examNum=int(input("How many exam grades each student have? "))
 if examNum>0:
  for i in range(examNum):
    examGrade=float(input("Enter the exam grades: ")) 
    total=total+examGrade
  average=total/examNum
  print("The average is ",average)
 anotherStud=input("Enter exam grades for another student(y/n)? ").lower()
 if anotherStud != "y":
  break
   


