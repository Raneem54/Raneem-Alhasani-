dic= { "Sunday": 30 ,
        "Moday": 29 ,
         "Tuesday": 31,
    "Wednesday": 33 ,
    "Thursday": 35 ,
    "Friday": 28 ,
    "Saturday": 25 ,
    
    }
total=0
for key in dic:
    total=total + dic[key]
avg= total/len(dic)
#-------------------------------------
maxm=0
for value in dic.values():
    if value > maxm:
        maxm=value
#---------------------------------------
for item in dic.items():
     print(item[0], item[1])
     if item[1] == maxm:
         print("this temp was on day : ", item[0])
#----------------------------------------
for day , temp in dic.items():
    if temp ==maxm:
     print(day)


















lastweekwether=[]
for key in dic:
    lastweekwether.append((key,dic[key]))
