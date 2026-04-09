import re
text="RaneeSalimAlhasani"
result=re.split('(?=[A-Z])',text)
print(result)