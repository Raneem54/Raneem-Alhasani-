infile=open('C:/Users/USER 1/Documents/python/s.txt','r')
line=infile.readline()

count=1
while line != "":
    print(line)
    line=infile.readline()
    count+=1
    print("number of lines= ", count)









infile.close()