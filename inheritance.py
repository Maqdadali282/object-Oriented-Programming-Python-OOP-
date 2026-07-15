class Bottle:
    def __init__(self, name, taste, color, price):
        print("inside constructor")
        self.name = name
        self.taste = taste
        self.color = color
        self.price = price

class Sting(Bottle):
    pass

b1 = Bottle("sting","best","red",150)
print("cool drink name is",b1.name)
print("the taste is ",b1.taste)
print("the solor is ",b1.color)
print("and the price is ",b1.price)