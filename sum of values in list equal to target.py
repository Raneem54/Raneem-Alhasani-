values=[3,2,4,6,1]
target=6
for i in values:

 for value in range(len(values)):
   if values[value]+ i ==target and values[value]!= i :
    print (values[value])

#another solution (better):
v=[3,2,4,1,0,6]
target=7
for i in range(len(v)):
    for j in range(i+1, len(v)):
        if v[i] +v[j] == target:
            print(v[i] , v[j])