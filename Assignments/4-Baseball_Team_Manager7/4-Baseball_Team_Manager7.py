import db

#region -- VALIDATE USER INPUT FUNCTIONS

# VALID POSITIONS TUPLE
valid_positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

# Function to get a valid player position from the user
def get_player_position():
    valid_positions_str = ', '.join(valid_positions)
    while True:
        position = input(f"Position ({valid_positions_str}): ")
        if position in valid_positions:
            return position
        else:
            print("Invalid position. Please choose from the valid positions above.")

# Function to get valid at bats from the user
def get_at_bats():
    while True:
        at_bats = input("At Bats: ")
        if at_bats.isdigit() and int(at_bats) >=0:
            return  int(at_bats)
        else:
            print("Invalid value for At Bats. Please enter a non-negative integer.")

# Function to get valid hits from the user compared to their at bats
def get_hits(at_bats):
    while True:
        hits = input("Hits: ")
        if hits.isdigit() and 0 <= int(hits) <= at_bats:
            return  int(hits)
        else:
            print("Invalid value for Hits. Please enter a non-negative integer less than or equal to At Bats.")
#endregion

#region -- NON-MENU FUNCTIONS --

# Function to get the player's position number
def get_lineup_number(players, prompt):
    while True:
        try:
            position = int(input(prompt))
            if 1 <= position <= len(players):
                return position
            else:
                print("Invalid input. Please select a valid lineup number.")
        except ValueError:
            print("Invalid input. Please select a valid lineup number.")

# Function to calculate batting average
def get_batting_avg(at_bats,hits):
    if at_bats == 0:
        return 0.0
    batting_avg = round(hits / at_bats, 3)
    return batting_avg
#endregion

#region -- MENU FUNCTIONS --

# 1 - Function to display the lineup
def display_lineup(players):
    if not players:
        print("The lineup is currently empty.\n")
    else:
        print(f"{'# ':<5}{'Player ':<10}{'Position ':<10}{'At Bats ':<10}{'Hits ':<10}{'Avg ':<10}")
        display_separator_thin()
        for i, player in enumerate(players, start=1):
            player_name = player[0]
            position = player[1]
            at_bats = int(player[2])  # Convert to integer
            hits = int(player[3])     # Convert to integer
            avg = get_batting_avg(at_bats, hits)
            print(f"{i:<5}{player_name:<10}{position:<10}{at_bats:<10}{hits:<10}{avg:<10.3f}")

# 2 - Function to add a new player to the lineup
def add_player(players):
    player_name = input("Name: ")
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    
    player = [player_name, position, at_bats, hits]
    players.append(player)
    print(f"{player_name} was added. \n")

# 3 - Function to remove a player
def delete_player(players):
    if not players:
        print("The lineup is currently empty. There are no players to remove.")
        return

    print("\nSelect a player to delete:")
    for i, player in enumerate(players):
        print(f"{i + 1}: {player[0]} ({player[1]})")

    position = get_lineup_number(players, "\nEnter the number of the player to remove: ")
    deleted_player = players.pop(position - 1)
    print(f"{deleted_player[0]} has been removed from the lineup.\n")

# 4 - Function to move a player's lineup #
def move_player(players):
    if not players:
        print("The lineup is currently empty. There are no players to move.")
        return

    print("\nSelect a player to move:")
    for i, player in enumerate(players):
        print(f"{i + 1}: {player[0]} ({player[1]})")

    from_position = get_lineup_number(players, "\nEnter the number of the player to move: ")
    to_position = get_lineup_number(players, "Enter the new lineup number: ")
    player_to_move = players.pop(from_position - 1)
    players.insert(to_position - 1, player_to_move)
    print(f"{player_to_move[0]}'s lineup number was changed to {to_position}.\n")

# 5 - Function to change a player's position
def edit_player_position(players):
    if not players:
        print("The lineup is currently empty. There are no player positions to change.")
        return

    print("\nSelect a player to change their position:" )
    for i, player in enumerate(players):
        print(f"{i + 1}: {player[0]} ({player[1]})")
    
    position = get_lineup_number(players, "\nEnter the number of the player to change their position: ")
    new_position = get_player_position()
    players[position -1][1] = new_position
    print(f"{players[position - 1][0]}'s role was updated to {new_position}.")

# 6 - Function to change a player's stats
def edit_player_stats(players):
    if not players:
        print("The lineup is currently empty. There are no player stats to change.")
        return

    print("\nSelect a player to change their stats:" )
    for i, player in enumerate(players):
        print(f"{i + 1}: {player[0]} ({player[1]})")
    
    position = get_lineup_number(players, "Enter the number of the player to change their stats: ")
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    players[position -1][2] = at_bats
    players[position -1][3] = hits
    print(f"{players[position - 1][0]}'s stats were updated.")

 #endregion   

#region -- MENU ELEMENTS --

# THICK SEPARATOR LINE
def display_separator_thick():
    print("=" *56)

# THIN SEPARATOR LINE
def display_separator_thin():
    print("-" *56)

# TITLE
def display_title():
    print(" " *20 + "Baseball Team Manager")

# MENU OPTIONS
def display_menu():
    print("\nMENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Show menu")
    print("8 - Exit program")

# POSITIONS (DISPLAY)
def display_positions():
    print("POSITIONS")
    for i, position in enumerate(valid_positions):
        if i == len(valid_positions) - 1:
            print(position)
        else:
            print(position, end=', ')
#endregion

#region -- MAIN FUNCTION --
def main():
    display_separator_thick()
    display_title()
    display_positions()
    display_separator_thick()
    
    players = db.read_players()  # Use the db module to read players
    display_menu()  # Display the menu initially

    while True:
        menu_option = int(input("Menu option: "))
        if menu_option == 1:
            display_lineup(players)
        elif menu_option == 2:
            add_player(players)
        elif menu_option == 3:
            delete_player(players)
        elif menu_option == 4:
            move_player(players)
        elif menu_option == 5:
            edit_player_position(players)
        elif menu_option == 6:
            edit_player_stats(players)
        elif menu_option == 7:
            display_menu()
        elif menu_option == 8:
            print("Exiting the program.")
            break
        else:
            print("Invalid menu option. Please choose a valid option.")

        db.write_players(players)

# endregion

if __name__ == "__main__":
    main()
