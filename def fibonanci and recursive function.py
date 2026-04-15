def fibonanci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonanci(n-1) +fibonanci(n-2)
print(fibonanci(8))