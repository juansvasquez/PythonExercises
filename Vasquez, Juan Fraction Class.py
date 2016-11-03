def gcd(x,y):
    while y != 0:
        (x,y) = (y,x%y)
    return x

class Fraction:
    def __init__(self,n,d):
        z = gcd(n,d)
        self.num = n//z
        self.den = d//z
        
    def decimalApprox(self):
        return self.num/self.den

    def __mul__(self, other):
        newNum = self.num*other.num
        newDen = self.den*other.den
        newF = Fraction(newNum,newDen)
        return newF

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        den = self.den*other.den
        num = self.num*other.den+other.num*self.den
        return Fraction(num,den)

    def __gt__(self, other):
        if self.num/self.den>other.num/other.den:
            return True
        else:
            return False
    def addInteger(self,x):
        nInt = self.den*x
        num = nInt+self.num
        return Fraction(num,self.den)
    
f1 = Fraction(4,6)
f2 = Fraction(1,5)
y = f1.decimalApprox()
z = f2.decimalApprox()
f3 = f1*f2
f4 = f1+f2
g = (f1>f2)
i = f2.addInteger(-2)
print(y)
print(z)
print(f1)
print(f2)
print(f3)
print(f4)
print(g)
print(i)
