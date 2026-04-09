def oufunc(a,b):
    
    def innfunc(a,b):
        return a+b
    return innfunc(a,b) +5

print(oufunc(1,2))
