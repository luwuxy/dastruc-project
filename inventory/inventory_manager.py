
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
        self._quantity = quantity
    
    def setQuantity(self, quantity = 1): 
        self._quantity = quantity

    def getQuantity(self): 
        return self._quantity

    def setID(self, id): 
        self._id = id

    def getID(self): 
        return self._id
    
    def __str__(self):
        return (f"ID: {self.getID()} \n"
            f"Name: {self.name} \n"
            f"Expiry: {self.expiry.date()} \n"
            f"Quantity: {self.getQuantity()} \n"
            f"Calories: {self.calories} \n"
            f"Protein: {self.protein} \n"
            f"Vitamins: {self.vitamins} \n"
            f"Fats: {self.fats}")
    

#Inventory manager class
class Inventory:
    def __init__(self): #constructor
        self.items = {} #dictionary that stores all the food items

    #function for adding item to inventory
    def add_item(self,id, name, expiry, calories, protein, vitamins, fats, quantity): 
        if id in self.items:
            return f"Item ID '{id}' already exists. Please use a unique ID."

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
        while True:
            id = input("Enter a unique food item ID to complete: ").strip().upper()
            if id in self.items:
                print("❗ This ID already exists. Please enter a different one.")
            else:
                break

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
    
    def reduce_qty(self, qty_chosen, food_obj):
        if qty_chosen > food_obj.getQuantity():
            return "Insufficient stock"
        food_obj.setQuantity(food_obj.getQuantity() - qty_chosen)
        return True

    def increase_qty(self, item_id, qty_to_add, expiry):
        item = self.items.get(item_id)
        if not item:
            return f"Item ID {item_id} not found in inventory."
        try:
            expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

        if item.expiry != expiry_date:
            return (f"❗ Expiry date mismatch. Existing item expires on {item.expiry.date()}.\n"
                    f"Please add it as a new batch.")

        item.setQuantity(item.getQuantity() + qty_to_add)
        return f"Restocked {qty_to_add} units of {item.name}. New quantity: {item.getQuantity()}"

        
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







