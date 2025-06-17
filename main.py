from beneficiary_tracker.beneficiary import Beneficiary
from beneficiary_tracker.beneficiary_manager import BeneficiaryManager
from inventory.inventory_manager import Inventory
from distributor.distributor import Distributor

manager = BeneficiaryManager()
inventory = Inventory()


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
            distribution_menu()
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
            else:
                print("No beneficiary was found.")
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


def distribution_menu():
    distributor = Distributor(inventory, manager)

    while True:
        print("""
[==================================]       
Distribution Menu
1. Distribute to a beneficiary (auto-match)
2. Distribute to all beneficiaries (auto-match)
3. Manual distribution
4. Go back
[==================================]\n""")
        
        option = input("Please choose an option: ").strip()
        print("")

        if option == "1":
            beneficiary_id = input("Enter the Beneficiary ID: ").strip()
            beneficiary = manager.get(beneficiary_id)
            if beneficiary:
                food_pack, summary = distributor.match_food_to_needs(beneficiary)
                if food_pack:
                    ticket = distributor.create_ticket(beneficiary_id, food_pack)
                    distributor.distribution_tickets.append(ticket)
                    print(f"✅ Distributed to {beneficiary.name} (ID: {beneficiary.id})")
                    print("Included in food pack:")
                    print(summary)
                    distributor.print_and_export_ticket(ticket)
                else:
                    print("Could not create a matching food pack for this beneficiary.")
            else:
                print("Beneficiary not found.")
        
        elif option == "2":
            distributor.distribute()

        elif option == "3":
            distributor.manual_distribute()
        
        elif option == "4":
            break

        else:
            print("Invalid option, please try again.")



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
            fats = int(require_input("- Required Fats: "))
            break
        except ValueError:
            print("Fats must be a number!")
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
        "fats": fats,
        "calories": calories,
        "protein": protein,
        "vitamins": vitamins_list
    }
    # generate a random beneficiary id
    beneficiary_id = manager.generate_id()

    return Beneficiary(beneficiary_id, name, contact_info, needs)


# main call function
if __name__ == "__main__":
    inventory.add_item("VEG25001", "Broccoli", "2025-06-10", 3, 55, 4, ["C", "K"], 25)
    inventory.add_item("FRU25002", "Banana", "2025-06-12", 1, 90, 1, ["B6", "C"], 40)
    inventory.add_item("CHK25003", "Chicken Breast", "2025-07-01", 8, 165, 31, ["B12", "D"], 30)
    inventory.add_item("RCE25004", "White Rice", "2026-12-31", 1, 200, 4, ["B1"], 100)
    inventory.add_item("BRD25005", "Whole Wheat Bread", "2025-06-30", 2, 120, 5, ["B", "E"], 20)
    inventory.add_item("MLK25006", "Powdered Milk", "2025-09-15", 5, 100, 6, ["A", "D", "B12"], 15)
    inventory.add_item("EGG25007", "Egg", "2025-06-25", 5, 70, 6, ["D", "B12"], 60)
    inventory.add_item("VGT25008", "Malunggay Leaves", "2025-06-08", 1, 35, 3, ["A", "C", "E"], 10)
    inventory.add_item("FIS25009", "Canned Tuna", "2026-01-20", 5, 190, 20, ["D", "B12"], 35)
    inventory.add_item("LEG25010", "Lentils", "2026-03-01", 1, 230, 18, ["B9", "Iron"], 40)
    inventory.add_item("VEG25011", "Carrots", "2025-06-15", 0, 41, 1, ["A", "K"], 50)
    inventory.add_item("OIL25012", "Vegetable Oil", "2025-12-10", 14, 120, 0, [], 20)
    inventory.add_item("APP25013", "Apple", "2025-06-09", 0, 95, 0, ["C"], 30)
    inventory.add_item("BRN25014", "Brown Rice", "2026-10-01", 2, 215, 5, ["B3", "Magnesium"], 60)


    main_menu()
