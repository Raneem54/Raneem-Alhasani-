RATE=5
INITIAL_BALANCE=10000

numYears=int(input("Enter number of years: "))
balance=INITIAL_BALANCE
for year in range(1, numYears +1):
    interest=balance*RATE/100
    balance=balance+interest
    print("%d %10.2f" % (year, balance))