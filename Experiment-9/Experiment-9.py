#(I) :

a = int(input("Enter x: "))
b = int(input("Enter y: "))

LHS = (x + y) ** 2
RHS = a**2 + 2*a*b + b**2

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#(II) :
x = 12
y = 17

LHS = (x - y) ** 2
RHS = x**2 - 2*x*y + y**2

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#(III):
x = 6
y = 14

LHS = (x + y) * (x - y)
RHS = x**2 - y**2

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#(IV):
x = 5
y = 7

LHS = x**3 + y**3
RHS = (x + y) * (x**2 - x*y + y**2)

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#Addition using Bitwise: 
x = 2
y = 6

LHS = x + y
RHS = (x ^ y) + 2*(x & y)

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)

#Subtraction:
x = 6
y = 5

LHS = x - y
RHS = (x ^ y) - ((x & y) << 1)

print("LHS =", LHS)
print("RHS =", RHS)
print("Equal =", LHS == RHS)
