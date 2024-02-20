name = (input("enter your name please: "))

a = int(input("enter a value for a: "))
b = int(input("enter a value for b: "))
c = int(input("enter a value for c: "))
d = int(input("enter a value for d: "))

def solvecubic(a,b,c,d):
    root= (x)
    return(root)

bracket1= ((-b**3) / (27*a**3) + (b*c) / (6*a**2) - (d) / (2*a))
bracket2= (c) / (3*a) - (b**2) / (9*a**2)
bracket3= (-b) / (3*a)

x = ((bracket1 + (bracket1**2)+ bracket2**3) ** 1/3 ) + ((bracket1 - bracket1 **2 + bracket2**3) ** 1/3) - (bracket3)

print(" Hello" , name, "I will sollve x^3-6x^+11x-6=0")
print(solvecubic(a,b,c,d))




quit()

