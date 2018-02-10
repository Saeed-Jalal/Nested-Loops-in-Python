#Nested loops ,Python allows us to use loop inside another loop
#Nested while loop
print("Welcome to Jalalians Bank of EU ATM!")
restart = ("Y","Yes")
chances = 3
balance = 10000.50
while chances >= 0:
    pin = int(input("Please enter your 4 digit Pin code: "))
    if pin == (1122):
        print("You have entered your Pin correctly.\n ")
        while restart not in ("No","no"):
            print("Press 1 For Your account Balance\n")
            print("Press 2 For Withdrawl Cash\n")
            print("Press 3 For Deposit Cash\n")
            print("Press 4 for Card Return\n")
            option = int(input("What would you like to Start."))
            if option == 1:
                print("Your account Balance is € ",balance,"\n")
                restart= input("Would you like to choose an other service.")
                if restart in ("No","no"):
                    print("Thank you for using our Services.")
                    break
            elif option == 2:
                option2 =("Y","Yes")
                withdrawl = float(input("How much Cash you want to withdraw. \n €10/€20/€40/€80/€100/€150"))
                if withdrawl in [10,20,40,80,100,150]:
                    balance = balance - withdrawl
                    print("\n Your remaining Balance is now €",balance)
                    restart = input("Would you like to choose an other service.")
                    if restart in ("No","no"):
                        print("Thank you for using our Services.")
                        break
                elif withdrawl != [10,20,40,80,100,150]:
                    print("Invalid Amount, Please try again.\n")
                    restart = ("Y","Yes")
                elif withdrawl == 1:
                    withdrawl = float(input("Enter your Amount:"))

            elif option == 3:
                Deposit = float(input("How much you want to Deposit."))
                balance = balance + Deposit
                print("\nYour Balance is now €",balance)
                restart = input('Would you like to choose an other Service.')
                if restart in ('No','no'):
                    print('Thank you for using our Services.')
                    break
            elif option == 4:
                print("Please wait while your card is returned...\n")
                print("Thank you for using our Services.")
                break
            else:
                print("Please choose the correct option number. \n")
                restart = ("Y","Yes")
    elif pin != ("1122"):
        print("Sorry,Wrong Pin code")
        chances = chances -1
        if chances == 0:
            print("\nSorry,No more tries")
            break

#Nested for loop
from math import sqrt
n = int(input("Number: "))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 +b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2)== 0):
            print(a,b,c)

#Nested for loop inside the while loop
trip_start = input("Are you having a trip! yes or no:")
while trip_start == "yes":
    number = int(input("How many people:"))
    for number in range(1,number+1):
        name = input("Name of traveler:")
        age = input("Age")
        sex = input("Male or Female:")
        print(name)
        print(age)
        print(sex)
    trip_start = input("Did, You forgot someone?")
else:print("Have a nice trip.")

