import time
from datetime import datetime

print("WELCOME TO ATM")
time.sleep(2)

print("Insert your card")
time.sleep(2)

password = 6398
balance = 5000
daily_limit = 10000
withdrawn_today = 0

try:
    pin = int(input("Enter your card PIN: "))
except:
    print("Invalid PIN")
    exit()

if pin == password:
    while True:
        print("""
        ===== ATM MENU =====
        1. Check Balance
        2. Withdraw Amount
        3. Deposit Amount
        4. Exit
        """)
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Invalid input")
            continue

        if option == 1:
            print(f"Your current balance is ₹{balance}")

        elif option == 2:
            withdraw_amount = int(input("Enter withdraw amount: "))

            if withdrawn_today + withdraw_amount > daily_limit:
                print("Daily withdrawal limit exceeded")
                continue

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                withdrawn_today += withdraw_amount

                print(f"₹{withdraw_amount} withdrawn successfully")
                print("\n----- ATM RECEIPT -----")
                print("Transaction Type : Withdrawal")
                print(f"Amount           : ₹{withdraw_amount}")
                print(f"Date & Time      : {datetime.now()}")
                print(f"Available Balance: ₹{balance}")
                print("------------------------\n")

            else:
                print("Insufficient balance")
        elif option == 3:
            deposit_amount = int(input("Enter deposit amount: "))
            balance += deposit_amount

            print(f"₹{deposit_amount} deposited successfully")
            print("\n----- ATM RECEIPT -----")
            print("Transaction Type : Deposit")
            print(f"Amount           : ₹{deposit_amount}")
            print(f"Date & Time      : {datetime.now()}")
            print(f"Available Balance: ₹{balance}")
            print("------------------------\n")

        elif option == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Invalid request")
