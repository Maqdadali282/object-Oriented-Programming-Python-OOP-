class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0

        self.menu()
    
    def menu(self):
        user_input=input(""" 
        Hello, How would you like to proceed?
        1.Enter 1 to create pin
        2.Enter 2 to deposite 
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5.Exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            self.exit()

    def create_pin(self):
        self.pin=input("Enter your pin : ")
        print("Pin set succesfully!")
        self.menu()
    
    def deposit(self):
        temp= input("Enter your pin : ")
        if temp == self.pin:
            amount = int(input("Enter your amount you want to deposit : "))
            self.balance = self.balance + amount
            print("deposit succesfully")
        else:
            print("invalid pin")
        self.menu()


    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw : "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdraw success")
            else:
                print("unsuffcient belance!")
        else:
            print("invalid balance")
        self.menu()
    
    def check_balance(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        self.menu()
    
    def exit(self):
        print("Goodbye")
        exit()

atm = Atm()
        