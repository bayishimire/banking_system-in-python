from registrationsystem.register import system

class Deposit:

    def deposit(self, name, amount):

        for user in system.store:

            if user["name"] == name:

                # Initialize balance if not exists
                if "balance" not in user:
                    user["balance"] = 0

                if amount > 0:
                    user["balance"] += amount
                    print(f"Deposit successful. New balance: {user['balance']}")
                    return

                else:
                    print("Invalid deposit amount")
                    return

        print("User not found")