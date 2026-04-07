count=0
number =input("Enter a number:")
while count < len(number):
    if int(number[count])%2==0:
        print(number[count])
    count=count+1

    