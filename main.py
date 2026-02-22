from registrationsystem.register import system
from registrationsystem.system.deposit import Deposit

def main():

    condition = True

    # Create database account handler
    account = system("","")

    deposit_service = Deposit()

    while condition:

        print("\n====== BANK MENU ======")
        print("1. Register")
        print("2. Login")
        
        choice = int(input("Choose option: "))

        # Register
        if choice == 1:

            username = input("Enter username: ")
            pwd = input("Enter password: ")

            account.register(username, pwd)

        # Login
        elif choice == 2:

            username = input("Enter username: ")
            pwd = input("Enter password: ")

            account.name = username

            if account.login(pwd):
                print("Login successful")
                print("Welcome", username)
                print("\n == services==")
                print("3. Deposit")
                print("4. Withdraw")
                print("5. Show Database")
                print("0. Exit")
                while(condition):

                    choice = int(input("Choose option: "))

                    if choice == 3:

                     name = input("Enter username: ")
                     amount = int(input("Enter deposit amount: "))

                     deposit_service.deposit(name, amount)   

                    elif choice == 4:
                     print("Withdraw service not implemented yet")

                    elif choice == 5:
                    
                     print(system.store)
                    elif choice == 0:
                      print("Goodbye")
                      condition = False
                    
                    

            else:
                print("Login failed")
                condition = False

        # Deposit
        # elif choice == 3:

        #     name = input("Enter username: ")
        #     amount = int(input("Enter deposit amount: "))

        #     deposit_service.deposit(name, amount)

        # Withdraw (You must create Withdraw class similarly)

        # elif choice == 4:
        #     print("Withdraw service not implemented yet")

        # # Show database
        # elif choice == 5:
        #     print(system.store)

        

        # else:
        #     print("Invalid choice")



if __name__ == "__main__":
    main()