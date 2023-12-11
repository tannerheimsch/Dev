import db
from datetime import date, datetime
from objects import Player, Lineup

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
def get_lineup_number(lineup, prompt):
    while True:
        try:
            position = int(input(prompt))
            if 1 <= position <= lineup.count:
                return position
            else:
                print("Invalid input. Please select a valid lineup number.")
        except ValueError:
            print("Invalid input. Please select a valid lineup number.")


# Function to calculate batting average
def get_batting_avg(player):
    return player.battingAvg()
#endregion

#region -- MENU FUNCTIONS --

# 1 - Function to display the lineup
def display_lineup(players):
    players = db.get_players()  # Retrieve players from the database

    if not players:
        print("The lineup is currently empty.\n")
    else:
        print(f"{'# ':<5}{'Player ':<20}{'Position ':<10}{'At Bats ':<10}{'Hits ':<10}{'Avg ':<10}")
        display_separator_thin()

        for i, player in enumerate(players, start=1):
            player_name = player.fullName
            position = player.position
            at_bats = player.atBats
            hits = player.hits
            avg = player.battingAvg
            print(f"{i:<5}{player_name:<20}{position:<10}{at_bats:<10}{hits:<10}{avg:<10.3f}")


# 2 - Function to add a new player to the lineup
def add_player(lineup):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)

    # Use the count property from the Lineup class
    playerID = lineup.count + 1

    player = Player(first_name, last_name, position, at_bats, hits, playerID)

    try:
        db.add_player(player)
        print(f"{player.fullName} added to the database.")
        lineup.add(player)
    except Exception as e:
        print(f"Error adding player to the database: {e}")
        return  # Stop further execution if there's an error with database operation

# 3 - Function to remove a player
def delete_player(lineup):
    if not lineup.count:
        print("The lineup is currently empty. There are no players to remove.")
        return

    print("\nSelect a player to delete:")
    for i, player in enumerate(lineup, start=1):
        print(f"{i}: {player.fullName} ({player.position})")

    position = get_lineup_number(lineup, "\nEnter the number of the player to remove: ")
    
    # Get the player from the lineup based on the selected position
    deleted_player = lineup.get(position)

    # Remove the player from the lineup
    lineup.remove(position)
    
    # Remove the player from the database
    db.delete_player(deleted_player)

    print(f"{deleted_player.fullName} has been removed from the lineup and the database.\n")

# 4 - Function to move a player's lineup
def move_player(lineup):
    if not lineup.count:
        print("The lineup is currently empty. There are no players to move.")
        return

    print("\nSelect a player to move:")
    for i, player in enumerate(lineup):
        print(f"{i + 1}: {player.fullName} ({player.position})")

    from_position = get_lineup_number(lineup, "\nEnter the number of the player to move: ")
    to_position = get_lineup_number(lineup, "Enter the new lineup number: ")
    
    # Get the player from the lineup based on the selected position
    player_to_move = lineup.get(from_position)

    # Move the player in the lineup
    lineup.move(from_position, to_position)

    # Update the player's lineup number in the database
    db.update_bat_order(lineup)

    print(f"{player_to_move.fullName}'s lineup number was changed to {to_position}.\n")

# 5 - Function to change a player's position
def edit_player_position(lineup):
    if not lineup.count:
        print("The lineup is currently empty. There are no player positions to change.")
        return

    print("\nSelect a player to change their position:")
    for i, player in enumerate(lineup):
        print(f"{i + 1}: {player.fullName} ({player.position})")

    position_number = get_lineup_number(lineup, "\nEnter the number of the player to change their position: ")
    new_position = get_player_position()

    # Get the player from the lineup based on the selected position
    player_to_edit = lineup.get(position_number)

    # Update the player's position in the lineup
    player_to_edit.position = new_position

    # Update the player's position in the database
    db.update_player(player_to_edit)

    print(f"{player_to_edit.fullName}'s position was updated to {new_position}.")


# 6 - Function to change a player's stats
def edit_player_stats(lineup):
    if not lineup.count:
        print("The lineup is currently empty. There are no player stats to change.")
        return

    print("\nSelect a player to change their stats:")
    for i, player in enumerate(lineup):
        print(f"{i + 1}: {player.fullName} ({player.position})")

    position_number = get_lineup_number(lineup, "Enter the number of the player to change their stats: ")

    # Get the player from the lineup based on the selected position
    player_to_edit = lineup.get(position_number)

    print(f"\nCurrent Stats for {player_to_edit.fullName}")
    print(f"Current At Bats: {player_to_edit.atBats}")
    print(f"Current Hits: {player_to_edit.hits}\n")

    # Get and validate new stats
    new_at_bats = get_at_bats()
    new_hits = get_hits(new_at_bats)

    # Update the player's stats in the lineup
    player_to_edit.atBats = new_at_bats
    player_to_edit.hits = new_hits

    # Update the player's stats in the database
    db.update_player(player_to_edit)

    print(f"\n{player_to_edit.fullName}'s stats were updated.")

 #endregion   

#region -- MENU ELEMENTS --

# THICK SEPARATOR LINE
def display_separator_thick():
    print("=" *56)

# THIN SEPARATOR LINE
def display_separator_thin():
    print("-" *70)

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

# DATES (DISPLAY)
def display_dates():
    print()

    date_format = "%Y-%m-%d"
    now = datetime.now()    
    current_date = datetime(now.year, now.month, now.day)
    print(f"CURRENT DATE:    {current_date.strftime(date_format)}")

    while True:
        game_date_str = input("GAME DATE:       ")
        if game_date_str == "":
            print()
            return

        try:
            game_date = datetime.strptime(game_date_str, date_format)
        except ValueError:
            print("Incorrect date format. Please try again.")
            continue
        
        time_span = game_date - current_date

        if time_span.days > -1:
            print(f"DAYS UNTIL GAME: {time_span.days}")
        print()
        break

#endregion

#region -- MAIN FUNCTION --
def main():
    players = db.get_players()
    lineup = Lineup()

    for player in players:
        lineup.add(player)
    
    display_separator_thick()
    display_title()
    display_dates()
    display_positions()
    display_separator_thick()
    display_menu()

    while True:
        menu_option = int(input("Menu option: "))
        if menu_option == 1:
            display_lineup(lineup)
        elif menu_option == 2:
            add_player(lineup)
        elif menu_option == 3:
            delete_player(lineup)
        elif menu_option == 4:
            move_player(lineup)
        elif menu_option == 5:
            edit_player_position(lineup)
        elif menu_option == 6:
            edit_player_stats(lineup)
        elif menu_option == 7:
            display_menu()
        elif menu_option == 8:
            print("Exiting the program.")
            break
        else:
            print("Invalid menu option. Please choose a valid option.")

        db.update_bat_order(lineup)  # Update bat order after any changes

# endregion

if __name__ == "__main__":
    main()