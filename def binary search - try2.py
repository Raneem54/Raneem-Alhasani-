values=[1,3,5,7,9,11]
def binary_search(number):
    midindex=len(values)//2

    if values[midindex]==number:
        print(midindex)


    elif values[midindex]<number:
        for element in range(midindex+1 , len(values)):
            if values[element]==number:
                print(element)


    elif values[midindex]>number:
        for element in range(midindex):
            if values[element]==number:
                print(element)
