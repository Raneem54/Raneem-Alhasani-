values=[1,3,5,7,9,11]
def binary_search(value):
    indexNum=len(values)//2
    if values[indexNum]==value:
        print(indexNum)
    elif values[indexNum]< value:
        for element in range(values[indexNum]+1,len(values)):
            if values[element]==value:
                print(values[element])
    
     elif values[indexNum]> value:
        for element in range(len(values)):
            if values[element]==value:
                print(values[element])   







index=(binary_search(values, 9))
print(index)