from utilities.csv_handler import read_csv
from utilities.path_handler import (
    get_csv_directory,
    get_round_images_directory,
    get_images_directory,
)
from models.championship import Championship


# Set up Championship with teams, restrictions, and images
def setup_championship():
    teams = read_csv(get_csv_directory() + "/teste.csv")
    cp = Championship("Campeonato Brasileiro 2024")

    for team in teams:
        cp.add_team(team[0], team[1], team[2])

    cp.create_restrictions()
    cp.generate_graph_coloring_image(get_images_directory())
    cp.generate_schedule(directory=get_round_images_directory())

    print("Championship set up and pairings generated.")
    input("Press any key to continue...")  # Pause and wait for user input
    return cp


# Print all rounds if Championship is set up
def print_all_rounds(cp):
    if cp:
        cp.print_all_rounds()
    else:
        print("Championship not set up. Exiting.")
        exit()


# Print program details
def print_program_information():
    print()
    print("University: Universidade de Brasília")
    print("Department: Computer Science")
    print("Course: Teoria e Aplicação de Grafos")
    print("Student: Guilherme Gomes Santa Rosa")
    print("Registration Number: 241017684")
    input("\nPress any key to return to the menu...")  # Pause and wait for user input


# Show the main menu
def display_menu():
    print("\nMenu:")
    print("1. Print all rounds")
    print("2. Program Information")
    print("3. Exit")


# Get and validate user choice
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an option: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid option. Enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Enter a number.")


# Handle user choices from the menu
def main_menu(cp):
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            print()
            print_all_rounds(cp)
            input(
                "Press any key to return to the menu..."
            )  # Pause and wait for user input
        elif choice == 2:
            print_program_information()
        elif choice == 3:
            print("Exiting the program.")
            break


# Initialize Championship and start menu
if __name__ == "__main__":
    cp = setup_championship()
    main_menu(cp)
