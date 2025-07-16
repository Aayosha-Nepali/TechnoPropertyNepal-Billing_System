from operations import *

def main():
    """
    This function is the main entry point of the program.
    It displays a menu with options to rent, return, or exit the program.
    Based on the user's input, it calls the appropriate functions to perform the desired action.
    """
    print("-" * 150)
    file_name = "data.txt"
    print("\t\t\t\t\t\t\tTechnoRental property\n")
    print("\t\t\t\t\t\t\t  Kathmandu, Nepal\n")
    print("\t\t\t\t\t\t9800780078 | technorental@gmail.com\n")

    print("-" * 150)
    print("Please choose from the options provided")
    print("-" * 150)
    print("Press 1 to rent ")
    print("Press 2 to return")
    print("Press 3 to exit")
    print("\n")

    data_dictionary = read(file_name)

    loop = True
    while loop:
        try:
            user_input = int(input("Enter the option you want to choose: "))
            if user_input == 1:
                data_table(file_name)
                rent_land(data_dictionary)
            elif user_input == 2:
                data_table(file_name)
                return_land(data_dictionary)
            elif user_input == 3:
                print("Thank you for visiting")
                break
            else:
                print("Please choose a correct option (1/2/3)")
        except ValueError:
            print()
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()
