def readbalancefile(balancefile):
    try:
        with open(balancefile, "r") as file:
            balance = file.read()
            return float(balance)
    except FileNotFoundError:
        balance = 0
        return balance


def writebalancefile(balancefile, balance):
    with open(balancefile, "w") as file:
        file.write(balance)
        
        
def menu():
        while True:
            try:
                print("Please choose one of the following transactions :")
                print("1. Check balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")
                choice = str(int(input("Your choice :")))
                if choice not in ["1", "2", "3", "4"]:
                    raise Exception
                else:
                    return choice
            except (ValueError, Exception):
                print("Invalid input.")

def menu2():
    while True:
            try:
                print("Please choose one of the following transactions :")
                print("1. Check balance")
                print("2. Deposit")
                print("3. Exit")
                choice = str(int(input("Your choice :")))
                if choice not in ["1", "2", "3"]:
                    raise Exception
                else:
                    return choice
            except (ValueError, Exception):
                print("Invalid input.")

def checkbalance(balance):
    print(f"Your current balance is {balance}")

def deposit(balance, balancefile):
    while True:
        try:
            amount = float(input("Please input an amount to deposit :"))
            print(amount)
            if amount <= 0:
                raise Exception
            else:
                updatedBalance = balance + amount
                writebalancefile(balancefile, str(updatedBalance))
                print(f"Your current balance is {updatedBalance}")
                return updatedBalance
        except Exception:
            print("Invalid input.")


def withdraw(balance, balancefile):
    while True:
        try:
            amount = float(input("Please input an amount to withdraw :"))
            if amount <= 0:
                raise Exception
            elif amount > balance:
                print("Insufficient funds")
                break
            else:
                updatedBalance = balance - amount
                writebalancefile(balancefile, str(updatedBalance))
                print(f"Your current balance is {updatedBalance}")
                return updatedBalance
        except Exception:
            print("Invalid input.")

def nextTxn():
    while True:
        try:
            nextxn = input("Do you have another transaction? [Y/N] :")
            if nextxn in ["Y", "y", "N", "n"]:
                return nextxn
            else:
                raise Exception
        except Exception:
            print("Invalid input.")

def exit():
    print("Thank you for choosing our bank. Goodbye.")
    nxttxn = "n"
    return nxttxn
