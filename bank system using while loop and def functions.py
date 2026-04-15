balance=10000
userName=input("Enter the username: ")
password=input("Enter the password: ")

def deposit(depositAmount):
    global balance
    balance=balance+depositAmount

def withdraw(withdrawAmount):
    global balance
    balance=balance-withdrawAmount

while userName != "admin" or password != "1234":
 print("Access Denied")
 userName=input("Enter the username: ")
 password=input("Enter the password: ")
 
print("Successfully loged in")
while True:
 serviceNum=int(input("Please choose a service from the given services by entering the number of the service \n 1. check balance \n 2. deposit money \n 3. withdraw money \n"))
 if serviceNum==1:
  print("The balance in your Account is ", balance)
 elif serviceNum==2:
  deposit(500)
  print(" your balace now ", balance)
 elif serviceNum==3:
  withdraw(600)
  print(" your balace now ", balance)


    