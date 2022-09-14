def factorial(x):
    C=1
    for i in range(1, x+1):
        C=C*i
    return C

n=int(input("n= "))
m=int(input("m= "))
if n<m:
    print("nedeterminat")
else:
    print("C=", factorial(n)/(factorial(m)*factorial(n-m)))
