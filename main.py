from beneficiary_tracker.beneficiary import Beneficiary
from beneficiary_tracker.beneficiary_manager import BeneficiaryManager
from inventory.inventory_manager import Inventory
from inventory.inventory_manager import FoodItem
from distributor.distributor import Distributor
from datetime import datetime

manager = BeneficiaryManager()
inventory = Inventory()


def main_menu():
    manager.load_data("beneficiaries.json")
    inventory.load_data("inventory.json")

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
            inventory_menu()
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
    inventory.save_data("inventory.json")


def inventory_menu():
    
    while True:
        print("""
[==================================]
Inventory Menu
1. Display Inventory
2. Add Item
3. Increase quantity of item
4. Search for an item
5. Back to home menu
[==================================]""")

        option = input("Select an option (1-5):").strip()

        if option == "1":
            inventory.remove_expired_items()
            inventory.display_inventory()
            inventory.save_data("inventory.json")

        elif option == "2":
            id, name, expiry, calories, protein, vitamins, fats, quantity = inventory.get_details()
            message = inventory.add_item(id, name, expiry, calories, protein, vitamins, fats, quantity)
            print(message)
            inventory.save_data("inventory.json")

        elif option == "3":
            item_id = input("Enter the ITEM ID to restock: ").strip().upper()

            if item_id not in inventory.items:
                print(f"❌ Item ID '{item_id}' does not exist in the inventory.")
                continue

            while True:
                try:
                    qty_to_add = int(input("Enter quantity to add: "))
                    if qty_to_add <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("❗ Please enter a valid positive integer.")

            while True:
                expiry = input("Enter expiry date for new stock (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(expiry, "%Y-%m-%d")
                    break
                except ValueError:
                    print("❗ Invalid date format. Please use YYYY-MM-DD.")

            message = inventory.increase_qty(item_id, qty_to_add, expiry)
            print(message)
            inventory.save_data("inventory.json")

        elif option == "4":
            sub_option = input("Search by: 1. ITEM ID  |  2. VITAMINS (Enter 1 or 2): ").strip()

            if sub_option == "1":
                item_id = input("Enter ITEM ID: ").strip()
                print(inventory.search_item_by_id(item_id))
                

            elif sub_option == "2":
                vitamin = input("Enter a vitamin/mineral (e.g., C or D): ").strip()
                res = inventory.search_item_by_vitamins(vitamin)
                if res:
                    print("🔎 Search results:")
                    inventory.display_table(res)
                else:
                    print("❌ No item found with that vitamin.")
            


        elif option == "5":
            main_menu()            
            break
        
        else:
            print("❗ Invalid search option.")



    
    
    


    
    














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
    main_menu()
