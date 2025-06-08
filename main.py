from beneficiary_tracker.beneficiary import Beneficiary
from beneficiary_tracker.beneficiary_manager import BeneficiaryManager

manager = BeneficiaryManager()


def main_menu():
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


def inventory_menu():
    while True:
        print("Inventory Menu")
        # more to be added

        option = input("Please choose an option: ")


def beneficiary_menu():
    while True:
        print("""
[==================================]
Beneficiary Menu
1. Add beneficiary
2. Remove beneficiary
3. List all beneficiaries
4. Go back
[==================================]""")

        option = input("Please choose an option: ")
        print("")
        print("====================================")

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
                if option == "":
                    break
        elif option == "4":
            break


def get_input():
    # I'm planning on making it so that it automatically generates the ID, I'll leave this as is for now
    beneficiary_id = input("Input beneficiary ID: ")
    name = input("Input beneficiary name: ")
    contact_info = input("Input contact info: ")

    print("Input dietary needs: ")
    calories = input("- Required Calories: ")
    protein = input("- Required Protein: ")
    vitamins = input("- Required Vitamins (separated by comma): ")
    vitamins_list = [v.strip().upper() for v in vitamins.split(",") if v.strip()]

    # define each dietary need using dictionary
    needs = {
        "calories": calories,
        "protein": protein,
        "vitamins": vitamins_list
    }

    return Beneficiary(beneficiary_id, name, contact_info, needs)


# main call function
main_menu()
