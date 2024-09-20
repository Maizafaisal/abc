print("WECOME TO MAIZA'S BANK ACCOUNNT")
print("Please insert your atm card")

pin=int(input("Enter your pin"))
balance=5000

if pin==1234:
    while True:
        print("1=check balance")
        print("2=Withdraw Money")
        print("3=Deposit Money")
        print("$=Exit")
        try:
            option=int(input("Choose any option obove"))
        except:
            print("please choose the valid option")

        if option == 1:
            print("----------")
            print(f"Your current balance is {balance}")
        if option == 2:
            withdrawmoney=int(input("Enter your withdraw amount"))
            print("----------")
            balance=balance-withdrawmoney
            print(f"{withdrawmoney} is debited from your account")
            print(f"Your current balance is {balance }")
        if option == 3:
            deposit_money=int(input("Enter your deposit"))
            balance=balance+deposit_money
            print("----------")
            print("{deposit_money} is credit to your account ")
            print("Your current balance is {balance}")
        if option == 4:
            print("THANKYOU FOR VISITING MY ACCOUNT....SEE YOU AGAIN")
            break

else:
    print("You entered the wrong pin....Try again")
