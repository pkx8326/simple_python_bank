def main():
    import functions as f
    balancefile = "balance.txt"
    print("Welcome to Python Bank.")
    
    nxttxn = ""
    while nxttxn not in ["N", "n"]:
        if f.readbalancefile(balancefile):
            balance = f.readbalancefile(balancefile)
            choice = f.menu()
            if choice == "1":
                f.checkbalance(balance)
                nxttxn = f.nextTxn()
                if nxttxn in ["N", "n"]:
                    nxttxn = f.exit()
            elif choice == "2":
                f.deposit(balance, balancefile)
                nxttxn = f.nextTxn()
                if nxttxn in ["N", "n"]:
                    nxttxn = f.exit()
            elif choice == "3":
                f.withdraw(balance, balancefile)
                nxttxn = f.nextTxn()
                if nxttxn in ["N", "n"]:
                    nxttxn = f.exit()
            else:
                nxttxn = f.exit()
        else:
            print("No balance file found. Please consider making a deposit with out bank.")
            balance = f.readbalancefile(balancefile)
            choice = f.menu2()
            if choice == "1":
                f.checkbalance(balance)
                nxttxn = f.nextTxn()
                if nxttxn in ["N", "n"]:
                    nxttxn = f.exit()
            elif choice == "2":
                f.deposit(balance, balancefile)
                nxttxn = f.nextTxn()
                if nxttxn in ["N", "n"]:
                    nxttxn = f.exit()
            else:
                nxttxn = f.exit()

if __name__ == "__main__":
    main()