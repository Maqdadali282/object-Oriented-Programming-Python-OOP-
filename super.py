# class Phone:
#     def __init__(self,price,brand,camera):
#         print("inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buy the phone")


# class SmartPhone(Phone):
#     def buy(self):
#         print("You bought a samrtphone")
#         super().buy()

# m1 = SmartPhone(50000,"iphone",13)
# m1.buy()

#2ne example
class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buy the phone")


class SmartPhone(Phone):
   def __init__(self,price,brand,camera,os,ram):
        print("pehle yahan")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram

s = SmartPhone(50000,"iphone",13,"Android",16)
print(s.os)
print(s.ram)