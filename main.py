from beneficiary_tracker.beneficiary import Beneficiary
from beneficiary_tracker.beneficiary_manager import BeneficiaryManager

manager = BeneficiaryManager()


def main_menu():
    manager.load_data("beneficiaries.json")

    while True:
        print("""
[==================================]
Welcome to the Food Bank System!
1. Manage Inventory
2. Manage Beneficiaries
3. Distribute Food
4. Exit Program
[==================================]""")
        option = input("Please choose an option: ")

        if option == "1":
            print("Nothing yet")
        elif option == "2":
            beneficiary_menu()
        elif option == "3":
            print("Nothing yet")
        elif option == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("That's not a valid option!")
    
    manager.save_data("beneficiaries.json")


def inventory_menu():
    while True:
        # put your inventory menu here, mas maganda if ibundle na natin lahat dito sa
        # main class yung interface para mas malinis yung ibang files. - Mar

        option = input("Please choose an option: ")


def beneficiary_menu():
    while True:
        print("""
[==================================]       
Beneficiary Menu
1. Add beneficiary
2. Remove beneficiary
3. List all beneficiaries
4. Search for beneficiary
5. Go back
[==================================]\n""")

        option = input("Please choose an option: ")
        print("")

        if option == "1":
            manager.add(get_input())
        elif option == "2":
            beneficiary_id = input("Input beneficiary ID to remove: ")

            if manager.get(beneficiary_id):
                manager.remove(beneficiary_id)
                print("Successfully removed beneficiary.")
        elif option == "3":
            while True:
                manager.show_all()

                option = input("Press enter to go back.")
                break
        elif option == "4":
            while True:
                search_value = input("Search beneficiaries (enter blank value to cancel): ")

                if search_value == "":
                    break
                elif search_value:
                    manager.search(search_value)
                else:
                    print(f"No beneficiary matches {search_value}.")
        elif option == "5":
            break


def get_input():
    # returns error if the user gives a blank input. ".strip() gets rid of any leading and trailing whitespace."
    def require_input(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            else:
                print("No input was given! Please enter a value.")

    name = require_input("Input beneficiary name: ")
    contact_info = require_input("Input contact info: ")

    print("Input dietary needs: ")
    # get input from user. if input is not an integer, it will return an exception, then repeat.
    while True:
        try:
            calories = int(require_input("- Required Calories: "))
            break
        except ValueError:
            print("Calories must be a number!")
    # same as above.
    while True:
        try:
            protein = int(require_input("- Required Protein: "))
            break
        except ValueError:
            print("Protein must be a number!")

    vitamins = require_input("- Required Vitamins (separated by comma): ")
    vitamins_list = [v.strip().upper() for v in vitamins.split(",") if v.strip()]

    # define each dietary need using dictionary
    needs = {
        "calories": calories,
        "protein": protein,
        "vitamins": vitamins_list
    }
    # generate a random beneficiary id
    beneficiary_id = manager.generate_id()

    return Beneficiary(beneficiary_id, name, contact_info, needs)


# main call function
if __name__ == "__main__":
    main_menu()
