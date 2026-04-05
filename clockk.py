h1=int(input("enter the hour for time1"))
m1=int(input("enter the minutes for time1: "))
h2=int(input("enter the hour for time2"))
m2=int(input("enter the minutes for time2: "))

if h1>0 and h1<23 and h2>0 and h2<23 and m1>=0 and m1<60 and m2>=0 and m2<60:
 Time1=(h1*60)+m1
 Time2=(h2*60)+m2
 if Time1>Time2:
    print("Time 2 comes first")
    
 elif Time2>Time1:
    print("Time 1 comes first")
    
 elif Time1==Time2:
     print("Time 1 and Time2 are same")
    
else:
    exit("Error, please try again")