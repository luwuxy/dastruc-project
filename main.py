from beneficiary_tracker.beneficiary import Beneficiary
from beneficiary_tracker.beneficiary_manager import BeneficiaryManager

def main_menu():
    while True:
      print("""
Welcome to the Food Bank System!
1. Manage Inventory
2. Manage Beneficiaries
3. Distribute Food
4. Exit Program
            """)
      option = input("Please choose an option: ")

      if option == "1":
         inventory_menu()
      elif option == "2":
         beneficiary_menu()
      elif option == "3":
         print("Chose 3")
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
Beneficiary Menu
1. Add a beneficiary
2. 
            """)
      # more to be added

      option = input("Please choose an option: ")

main_menu()