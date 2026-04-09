def sum_squares(n):
    summ=0
    for i in range(1,n+1):
     result=i**i
     summ=summ+result
    return summ
print(sum_squares(2))