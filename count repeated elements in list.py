values=[1,1,6,1,3,2,2,7]
check=[]
for i in values:
    rep=0
    if i not in check:
        for j in values:
            if i==j:
                 rep=rep+1
        check.append(i)
        if rep >1:
                 print(i, "repeated", rep,"Times")

 
    

