# #single level inheritance
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

# m1 = SmartPhone(50000,"iphone",13)
# m1.buy()

##Multi level inheritance
# class Product:
#     def review(self):
#         print("product review customer")

# class Phone(Product):
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

# s = SmartPhone(50000,"iphone",13)
# p= Phone(3000,"samsung",10)
# s.review()
# print(s.brand)
# p.review()

#hierarchy inheritance
class Hostel:
    def __init__(self,name,total_room):
        print("you are inside constructor")
        self.name = name
        self.total = total_room

    def open(self):
        print("the hostel is open")

class Kaka(Hostel):
    def close(self):
        print("hostel is close now")

class Shan(Hostel):
    def food(self):
        print("shan hostel has good food")

h = Shan("shan",20)
h.open()
print(h.name)
print(h.total)
h1 = Kaka("kakakhel",30)
h1.close()
print(h1.name)
print(h1.total)