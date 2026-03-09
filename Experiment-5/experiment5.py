# simple array values: 

x, y, z = (10, 20, 50)
print("The matrix is:")
print(x, y, z)
print("The value of x is:", x)
print("The value of y is:", y)
print("The value of z is:", z)


# Goals before match
player1, player2, player3 = (0, 0, 0)

print("\nThe goals before match:")
print("\nPlayer1  Player2  Player3")
print(player1, player2, player3)

print("\nGoals scored during the game:")

# Loop to update goals
for i in range(3):
    player1 = player1 + 1
    player2 = player2 + 2
    player3 = player3 + 3
    print(player1, player2, player3)