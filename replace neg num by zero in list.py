values=[1,-2,3,-4,5,6]
for value in range(len(values)):
    if values[value] <0:
        values[value]=0
print(values)