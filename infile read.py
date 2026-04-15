infile=open('C:/Users/USER 1/Documents/python/s.txt','r')
lines=infile.readlines()

for line in range(len(lines)):
    lines[line]=int(lines[line].strip())
print(lines)
average= sum(lines)/len(lines)
maximum=max(lines)
minimum=min(lines)
print(infile.read())