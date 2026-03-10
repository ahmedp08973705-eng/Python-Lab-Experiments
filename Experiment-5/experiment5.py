# simple array values: 

x, y, z = (10, 20, 50)
print("The matrix is:")
print(x, y, z)
print("The value of x is:", x)
print("The value of y is:", y)
print("The value of z is:", z)


# Goals before match
AHMED, OSMAN, MAZIN = (0, 0, 0)

print("\nThe goals before match:")
print("\nAHMED  OSMAN  MAZIN")
print(AHMED, OSMAN, MAZIN)

print("\nGoals scored during the game:")

# Loop to update goals
for i in range(3):
    AHMED = AHMED + 1
    OSMAN = OSMAN + 2
    MAZIN = MAZIN + 3
    print(AHMED, OSMAN, MAZIN)
