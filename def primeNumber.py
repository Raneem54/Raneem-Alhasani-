def primeNumber(number):
    if number<=1:
        return False
    
    count=2
    isPrime =True
    while count < number:
        if number % count ==0:
            isPrime= False
        count= count +1
    return isPrime 
print(primeNumber(5))
        