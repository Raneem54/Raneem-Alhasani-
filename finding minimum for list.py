values=[10,20,30]
minimum=values[0]

for value in values:
    if value < minimum:
        minimum=value
        
print(minimum)