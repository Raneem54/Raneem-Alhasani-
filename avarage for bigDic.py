bigDic = {
    "Ali": {"Math": 85, "Science": 78, "English": 92},
    "Sara": {"Math": 90, "Science": 88, "English": 85}
}
mark=[]
for names in bigDic:
    for subjects in names.values():
        if subjects not in mark:
            mark.append(dic[names])
