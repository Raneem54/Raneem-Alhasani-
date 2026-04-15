def multiply(lis,factor):
    lis=list(lis)
    for i in range(len(lis)):
        lis[i]=lis[i] * factor
    return lis
listt=[1,2,3]
factor=2
print(multiply(listt,factor))
print(listt)