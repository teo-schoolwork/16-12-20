password = input("What is your password?\n : ")
ticker = 0
exit = False

while password != 'abcd-!"£$' and ticker < 3:
    ticker += 1
    password = input("Incorrect. Please enter your password\n : ")


while ticker >= 3 and exit == False:
    print("Too many failed attempts. Please try again.")
    exit = True


while password == 'abcd-!"£$' and exit == False:
    print("Correct Password")
    exit = True
