players = ["Ahmed", "Mazin", "Osman"]
data = {}

for p in players:
    print("Enter status of", p)
    
    goals = int(input(f"{p} goals scored: "))
    games = int(input(f"{p} games played: "))
    
    avg = goals / games
    data[p] = avg

ahmed = data["Ahmed"]
mazin = data["Mazin"]
osman = data["Osman"]

# Ranking logic
if ahmed >= mazin and ahmed >= osman:
    first = "Ahmed"
    
    if mazin >= osman:
        second = "Mazin"
        third = "Osman"
    else:
        second = "Osman"
        third = "Mazin"

elif mazin >= ahmed and mazin >= osman:
    first = "Mazin"
    
    if ahmed >= osman:
        second = "Ahmed"
        third = "Osman"
    else:
        second = "Osman"
        third = "Ahmed"

else:
    first = "Osman"
    
    if ahmed >= mazin:
        second = "Ahmed"
        third = "Mazin"
    else:
        second = "Mazin"
        third = "Ahmed"

print("\nThe Rank of them is:")
print("1st player is =", first)
print("2nd player is =", second)
print("3rd player is =", third)