def bank_account_details(account_number,balance,date_of_opening):
        input("Customer Name:")
        print(f"{account_number}\n{balance}\n{date_of_opening}")

        print("To withdraw input withdraw, to deposit input deposit and to check your balance input check balance")
        wwylt=input("What would you like to do?:")
        w="withdraw"
        d="deposit"
        c="check balance"
        
        if wwylt == w:
            amount=int(input("How much:"))
            balance=balance-amount
            print(f"Thank you.Your balance is now {balance}")

        if wwylt == c:
            print(f"Your balance is {balance}")
            
        if wwylt == d:
            amount=int(input("How much:"))
            balance=balance+amount
            print(f"Your balance is now {balance}")
            
bank_account_details(6864,50000,"14/4/2024")