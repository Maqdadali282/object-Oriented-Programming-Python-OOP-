class Atm:
    __counter = 1
    def __init__(self):
        self.pin=" "
        self.balance = 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        print(id(self))

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter=new
        else:
            print("Not allowed")


ob1 = Atm()
print(ob1.sno)
Atm.set_counter(5)
print("counter : ",Atm.get_counter)