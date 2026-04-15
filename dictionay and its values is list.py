dic= { "Sunday": [30,29] ,
        "Monday": [29,31] ,
         "Tuesday": [31,30],
    "Wednesday": [33,32] ,
    "Thursday": [35,33] ,
    "Friday": [28,30] ,
    "Saturday": [25,23]
       }
for day, temps in dic.items():
    print(day, temps[0])
total =0

#Finding the averae tempratures for week 2:
#1' st method:
for value in dic.values():
 total=total + value[1]
 
avgWeek2=total/len(dic)

# adding values of week 3:
for day,temp in dic.items():
    temp3=int(input("enter week 3 temps: "))
    dic[day].append(temp3)
print(dic)

# adding values of week 3:
w3=[30,28,32,31, 32, 29, 26]
index=0
for key in dic.keys():
    dic[key].append(w3[index])
    index+=1


