balance=10000

def withdraw(amount):
    #This function intends to access the global 'balance' variable
    global balance
    if balance >= amount:
        balance=balance - amount
withdraw(350)
print("balance=",balance)