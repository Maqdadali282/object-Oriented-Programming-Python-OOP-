class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
    
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        temp_num = self.num * other.den + other.num * self.den 
        temp_den = self.den * other.den 
        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num = self.num * other.den - other.num * self.den 
        temp_den = self.den * other.den 
        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self,other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den 
        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self,other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num 
        return "{}/{}".format(temp_num,temp_den)

f1 = Fraction(4,5)
f2 = Fraction(6,7)
result1 = f1 + f2
result2 = f1 - f2
result3 = f1 * f2
result4 = f1 / f2

print("4/5 + 6/7 : ", result1)
print("4/5 - 6/7 : ", result2)
print("4/5 * 6/7 : ", result3)
print("4/5 / 6/7 : ", result4)