contacts={"fred" : [1000,2192] ,"mart":21282, "bob":2893 ,"sara":8298}

for key in contacts:
    
        
     if type(contacts[key]) is list:
      count=1
      for i in contacts[key]:
       print(key, contacts[key], count)
     else:
      print(key, contacts[key])
    