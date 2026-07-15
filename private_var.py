class Atm:
    def __init__(self):
        self.__pin="" # the two underscore before the pin and balance is indicate us private or privasy but in python we cannot do the complete privacy of any variable
        self.__balance=0

        self.__menu()
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if new_pin == str:
            self.__pin = new_pin
            return("Pin changed")
        else:
            return("not allowed")
        
    def __menu(self):
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
        self.__pin=input("Enter your pin : ")
        print("Pin set succesfully!")
        self.__menu()
    
    def deposit(self):
        temp= input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter your amount you want to deposit : "))
            self.__balance = self.__balance + amount
            print("deposit succesfully")
        else:
            print("invalid pin")
        self.__menu()


    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter the amount you want to withdraw : "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw success")
            else:
                print("unsuffcient belance!")
        else:
            print("invalid balance")
        self.__menu()
    
    def check_balance(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
        self.__menu()
    
    def exit(self):
        print("Goodbye")
        exit()

atm = Atm()
print(atm.get_pin())