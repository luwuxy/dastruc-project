# %%
from datetime import datetime
from tabulate import tabulate ##this is to display inventory in table format (this is tentative, and will be removed 
# if we decided to incorporate a GUI)
#class for each inidivual food item
class FoodItem:
    def __init__(self, name, expiry, calories, protein, vitamins, fats, quantity=1): 
        self.name = name 
        self.expiry =  datetime.strptime(expiry, "%Y-%m-%d")
        self.calories = calories
        self.protein = protein
        self.vitamins = vitamins
        self.fats = fats
        self.quantity = quantity

    def setID(self, id): 
        self._id = id

    def getID(self): 
        return self._id
    
    def __str__(self):
        return (f"ID: {self.getID()} \n"
            f"Name: {self.name} \n"
            f"Expiry: {self.expiry.date()} \n"
            f"Quantity: {self.quantity} \n"
            f"Calories: {self.calories} \n"
            f"Protein: {self.protein} \n"
            f"Vitamins: {self.vitamins} \n"
            f"Fats: {self.fats}")
#Inventory manager class
class Inventory:
    def __init__(self): #constructor
        self.items = {} #dictionary that stores all the food items (the actual inventory, in short)

    #function for adding item to inventory
    def add_item(self,id, name, expiry, calories, protein, vitamins, fats, quantity): 
        newItem = FoodItem(name, expiry, calories, protein, vitamins, fats, quantity)
        newItem.setID(id)
        self.items[newItem.getID()] = newItem #the food item created gets added to the inventory dictionary with the ITEM ID as
        # its key and the specified infos as its values 
        return f"{newItem.getID()}({name} added successfully!)"

    #function for searching a specific item in the inventory using ID
    def search_item_by_id(self, targetItem):
        if targetItem in self.items:
            return self.items.get(targetItem.upper())
        else:
            return f"Item with ID {targetItem} not found in inventory."
        
    def search_item_by_vitamins(self, targetVitamin):
        targetVitamin = targetVitamin.upper()
        results = []
        if self.items != None:
            for val in self.items.values():
                if targetVitamin in val.vitamins:
                    results.append(val)
            if results: 
                return results
            

    
    #function for displaying the inventory            
    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.📦")
            return

        self.display_table(self.items.values())        

    #function for prompting food item details from user           
    def get_details(self):
        name =  input("Enter the name of the food item:")
        quantity = int(input("Enter quantity:"))
        expiry = input("Enter expiry date (YYYY-MM-DD): ")
        print("Enter nutritional info:")
        calories = int(input("  Calories: "))
        protein = int(input("  Protein (grams): ")) 
        fats = int(input("  Fats: ")) 
        vits = input("Vitamins it is rich in(seperate it with comma)")
        vitamins = [v.strip().upper() for v in vits.split(",") if v.strip()] 
        id =  input("Enter the food item ID to complete: ")
        return id.upper(), name.upper(), expiry, calories, protein, vitamins, fats, quantity
    

    def display_table(self, item_list):
        if not item_list:
            print("📦 No items to display.")
            return
        
        table_data = []
        for item in item_list:
            table_data.append([
                item.getID(),
                item.name,
                item.expiry.date(),
                item.quantity,
                item.fats,
                item.calories,
                item.protein,
                item.vitamins
            ])
        
        headers = ["ID", "Name", "Expiry", "Quantity", "Fats", "Calories", "Protein", "Vitamins"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    
        
#hard coded - for testing purposes only!
 
inventory = Inventory()
#adding items to inventory
inventory.add_item("VEG25001", "Brocolli", "2025-06-10", 500, 150, "C,D,B12", 30, 20)
inventory.add_item("CHK25002", "Chicken", "2025-09-10", 800, 150, "A, B", 20, 50)
inventory.add_item("BRD25003", "White bread", "2028-09-11", 500, 150, "A", 10, 9)
#displaying
inventory.display_inventory() 
##searching for items with vitamin D
results = inventory.search_item_by_vitamins("a")
if results:
    print("RESULTS:")
    inventory.display_table(results)
else:
    print("No item found with that vitamin")
##searching for items with vitamin K
result2 = inventory.search_item_by_vitamins("k")
if result2:
    print("RESULTS:")
    inventory.display_table(result2)
else:
    print("No item found with that vitamin")
##searching for items with ITEMID
print(inventory.search_item_by_id("CHK25002"))
print(inventory.search_item_by_id("IWANNAKMS"))







