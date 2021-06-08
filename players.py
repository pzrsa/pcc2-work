# Prints the players starting from the 2nd last player
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[ : -2])

# Loops through each player until the third one, not all
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())