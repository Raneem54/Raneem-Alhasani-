List=["ali","muna","ahmed","reem","malak"]
List.append("")
newfriend="sara"
for i in range(len(List),1,):
    List[i]=List[i-1]
List[1]=newfriend
print(List)