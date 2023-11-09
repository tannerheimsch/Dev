# Display program title/menu options
print("==============================================================")
print("                    Baseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average\n2 - Exit program")
print("==============================================================")

while True:
    # Get input from the user
    menu_option = int(input("Menu option:\t"))

    if menu_option == 1:
        print("Calculate batting average...")
        at_bats = float(input("Official number of at bats:\t"))
        hits = float(input("Number of hits:\t"))
        player_avg = hits / at_bats
        print(f"Batting average for the player: {player_avg:.3f}\n")
    elif menu_option == 2:
        # Exit the program
        break
    else:
        print("Invalid menu option. Try again.\n")

# Exit program
print("Bye!")