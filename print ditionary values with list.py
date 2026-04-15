contacts={"fred" : [1000,2192] ,"mart":21282, "bob":2893 ,"sara":8298}
for item in contacts.items():
    
    
    if type(item[1]) is list:
        for i in range(len(item[1])):
          print(item[0],item[1][i],i+1)
    else:
        print(item[0],item[1])