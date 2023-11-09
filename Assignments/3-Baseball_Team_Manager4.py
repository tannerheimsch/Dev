# Function to display the separator line
def title_separator_line():
    print("==============================================================")

# Function to display the program title
def display_title():
    print("                    Baseball Team Manager")

# Function to display the menu options
def display_menu():
    print("MENU OPTIONS")
    print("1 - Calculate batting average\n2 - Exit program")

# Function to calculate batting average
def calculate_batting_average():
    print("Calculate batting average...")
    at_bats = float(input("Official number of at bats:\t"))
    hits = float(input("Number of hits:\t"))
    player_avg = hits / at_bats
    print(f"Batting average for the player: {player_avg:.3f}\n")

# Main function
def main():
    title_separator_line()
    display_title()
    display_menu()
    title_separator_line()

    while True:
        menu_option = int(input("Menu option:\t"))

        if menu_option == 1:
            calculate_batting_average()
        elif menu_option == 2:
            # Exit the program
            break
        else:
            print("Invalid menu option. Try again.\n")
            # Display the menu to let the user see valid options
            display_menu()

    print("Bye!")

if __name__ == "__main__":
    main()
