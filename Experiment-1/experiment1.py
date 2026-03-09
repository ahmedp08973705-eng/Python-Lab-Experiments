#(I) :

a = int(input("Enter A: "))
b = int(input("Enter B: "))

LHS = (a + b) ** 2
RHS = a**2 + 2*a*b + b**2

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#(II) :
a = 10
b = 15

LHS = (a - b) ** 2
RHS = a**2 - 2*a*b + b**2

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#(III):
a = 10
b = 15

LHS = (a + b) * (a - b)
RHS = a**2 - b**2

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#(IV):
a = 5
b = 7

LHS = a**3 + b**3
RHS = (a + b) * (a**2 - a*b + b**2)

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#Addition using Bitwise: 
a = 1
b = 2

LHS = a + b
RHS = (a ^ b) + 2*(a & b)

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#Subtraction:
a = 10
b = 8

LHS = a - b
RHS = (a ^ b) - ((a & b) << 1)

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

