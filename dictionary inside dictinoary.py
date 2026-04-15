records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]

dictionary={}
for element in range(len(records)):
    name=records[element][0]
    subject=records[element][1]
    mark=records[element][2]
    if name not in dictionary:
     dictionary[name]={}
     
    dictionary[name][subject]=mark
print(dictionary)

     
      
         
        