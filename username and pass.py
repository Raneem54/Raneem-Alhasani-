user=input("please enter the username: ")
if user=="admin":
    password=int(input("please enter the password"))
    if password==1234:
        print("Acsessed")
elif user=="guest":
    print("Access granted")
else:
    exit("Access not granted")