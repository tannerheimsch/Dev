# Display program message/explanation
print("============================================================== \n                    Baseball Team Manager")
print()
print("This program calculates the batting average for a player based \non the player's official number of at bats and hits.")
print("==============================================================")

# Get inputs from the user
player_name= (input("Player's name:\t"))
at_bats=float(input("Official number of at bats:\t"))
hits=float(input("Number of hits:\t"))

# Calculate avg and round to 3 decimal places
player_avg = hits / at_bats
player_avg_rounded = "{:.3f}".format(player_avg)

# Display the result
print()
print(f"{player_name}'s batting average is: {player_avg_rounded}")