import math
def perfectSqrt(num):
 root=math.sqrt(num)
 if root.is_integer():
    return root(num)
 else:
    return("Not perfect sqrt")
print(perfectSqrt(6))
        