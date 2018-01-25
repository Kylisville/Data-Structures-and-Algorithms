from fractions import Fraction
def reku(n):
    if n == 0:
        return 1
    else:
        return Fraction(1/(1+reku(n-1)))
print (reku(4))
