
balance=10000

userName=input("Enter the user name: ")
password=input("Enter your password: ")

if userName=="admin" and password=="1234":
    print("Successfully loged in")
    serviceNum=int(input("Please choose a service from the given services by entering the number of the service \n 1. check balance \n 2. deposit money \n 3. withdraw money \n"))
    if serviceNum==1:
        print("The balance in your Account is ", balance)
    elif serviceNum==2:
        depos=float(input("Enter the amount of deposition: "))
        balance=float(balance+depos)
        print(" your balace now ", balance)
    elif serviceNum==3:
        withdraw=float(input("Enter the amount of withdrawal: "))
        if withdraw <= balance:
            balance=float(balance-withdraw)
            print(" your balace now ", balance)
        else:
            print(" your balace is too low")
else:
    print("  denied access ")
    