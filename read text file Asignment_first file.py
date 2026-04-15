infile=open("C:/Users/USER 1/Documents/math/Math_16.txt","r")
line=infile.readline().strip()
print("The title is: ",line)

line2=infile.readline().strip()
print("The number of file is: ",line2)

print()
print("The description:")
for line in infile: 
 if "example" in line:
     break
 print(line.strip())
print()
 

for example in infile:
 if "Example" in example:
     print(example.strip())
     break
for example in infile:
    print(example.strip())
    