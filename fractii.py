from fractions import Fraction
i,j=eval(input('numitorul si numaratorul fractiei 1: '))
n,m=eval(input('numitorul si numaratorul fractiei 2: '))

a=Fraction(i,j)
b=Fraction(n,m)

def suma(a,b):
    S=a+b
    return S

def produs(a,b):
    P=a*b
    return P

print(a,"+",b,"=", suma(a,b))
print(a,"*",b,"=", produs(a,b))