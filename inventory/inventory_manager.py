
from datetime import datetime #needed for expiry date
from tabulate import tabulate #to display output in table formt
import heapq #for priority queue

#class for individual food items
class FoodItem:
    def __init__(self, name, expiry, calories, protein, vitamins, fats, quantity=1): #Food item constructor
        self.name = name 
        self.expiry =  datetime.strptime(expiry, "%Y-%m-%d")
        self.calories = calories
        self.protein = protein
        self.vitamins = vitamins
        self.fats = fats
        self._quantity = quantity

#getter and setter methods for private attributes (quantity and itemID)
    def setQuantity(self, quantity=1): 
        self._quantity = quantity

    def getQuantity(self): 
        return self._quantity

    def setID(self, id): 
        self._id = id

    def getID(self): 
        return self._id

#string representation of each food object    
    def __str__(self):
        return (f"ID: {self.getID()} \n"
            f"Name: {self.name} \n"
            f"Expiry: {self.expiry.date()} \n"
            f"Quantity: {self.getQuantity()} \n"
            f"Calories: {self.calories} \n"
            f"Protein: {self.protein} \n"
            f"Vitamins: {self.vitamins} \n"
            f"Fats: {self.fats}")
    

#Inventory class
class Inventory:
    def __init__(self): #Inventory constructor
        self.items = {} #dictionary that stores all the food items
        self.expiry_heap = [] #heap that store an ITEMID along with its expiry date, with the soonest expiring item at the first 

    #function for adding item to inventory
    def add_item(self,id, name, expiry, calories, protein, vitamins, fats, quantity): 
        newItem = FoodItem(name, expiry, calories, protein, vitamins, fats, quantity) #create a food object
        newItem.setID(id) #and set its unique ID
        self.items[newItem.getID()] = newItem #the new food item created gets added to the inventory with the ITEM ID as
        #its key and the the food object itself as the value 
        heapq.heappush(self.expiry_heap, (newItem.expiry, newItem.getID())) #once added, push the added item's ID and expiry date to the heap
        return f"{newItem.getID()}({name} added successfully!)"

    #function for searching a specific item using item ID
    def search_item_by_id(self, targetID):
        targetID = targetID.upper()
        if targetID in self.items: #if it exists, return its value
            return self.items.get(targetID)
        else:
            return f"Item with ID {targetID} does not exist in inventory."
        
    #function for searching items by entering a specific vitamin     
    def search_item_by_vitamins(self, targetVitamin):
        targetVitamin = targetVitamin.upper()
        results = [] #list for storing results
        if self.items != None: #if the inventory is not empty, 
            for val in self.items.values(): #loop through each food item
                if targetVitamin in val.vitamins: #and if that food item's vitamins matches the targetVitamin
                    results.append(val) #append the food item to the results
            if results: #if there's results, return it
                return results
    
    #function for displaying the inventory            
    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.📦")
            return
        
        #if inventory is not empty, sort it by expiry date
        sorted_items = sorted(self.items.values(), key=lambda item: item.expiry)
        self.display_table(sorted_items) #and display it in a table
    
#function for displaying in table format
    def display_table(self, item_list): 
        if not item_list: #if list is empty, 
            print("No items to display.")
            return
        
        table_data = []
        for item in item_list: #for each food object in the passed list, append its attributes to the table_data
            table_data.append([
                item.getID(),
                item.name,
                item.expiry.date(),
                item.getQuantity(),
                item.fats,
                item.calories,
                item.protein,
                item.vitamins
            ])
        #set the type of attribute as the headers for better readability
        headers = ["ID", "Name", "Expiry", "Quantity", "Fats", "Calories", "Protein", "Vitamins"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
#function for reducing the stock of an item
    def reduce_qty(self, qty_chosen, food_obj):
        if qty_chosen > food_obj.getQuantity(): #if the quantity chosen is greater than the current stock,
            return "Insufficient stock" 
        food_obj.setQuantity(food_obj.getQuantity() - qty_chosen) #if the quantity chosen is less than the current stock, deduct it
        return True
    
#function for updating the stock levels of an item with the same expiry date
    def increase_qty(self, item_id, qty_to_add, expiry):
        item = self.items.get(item_id)
        if not item:
            return f"Item ID {item_id} not found in inventory."
        try:
            expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

        if item.expiry != expiry_date: #if they have different expiry date, the new stocks cannot be added to the existing stocks
            return (f"Expiry date mismatch. Existing item expires on {item.expiry.date()}.\n"
                    f"Please add it as a new batch.")
        item.setQuantity(item.getQuantity() + qty_to_add) #but if same, update the stock level
        return f"Restocked {qty_to_add} units of {item.name}. New quantity: {item.getQuantity()}"
    
    
    #function for deleting the expired items every time the program starts
    def remove_expired_items(self):
        today = datetime.today().date() #get the current date
        removed = [] #list for storing removed items
        #while there's food in inventory, and the expiry date of the first item (soonest expiring item) in the heap is less than or equal to today
        while self.expiry_heap and self.expiry_heap[0][0].date() <= today:
            expiry, item_id = heapq.heappop(self.expiry_heap) #remove it from the heap
            if item_id in self.items: 
                item = self.items.pop(item_id) #and delete the item from the heap
                removed.append((item_id, item.name, expiry.date())) #append the deleted items to the removed list
    
        if removed: #if removed list is not empty- meaning expired items were removed, notify te user.
            print("🗑️ The following expired items were removed from the inventory:")
            for item_id, name, exp in removed:
                print(f" - {item_id} ({name}) [Expired: {exp}]")
        else: #if empty, print:
            print("🟢 No expired items found.")
    
    #function for getting food item details (for adding item)
    def get_details(self):
        name = input("Enter the name of the food item: ").strip()
        while not name:
            print("❗ Name cannot be empty.")
            name = input("Enter the name of the food item: ").strip()

        # Validate quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("❗ Please enter a valid positive integer for quantity.")

        # Validate expiry date
        while True:
            expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(expiry, "%Y-%m-%d")
                break
            except ValueError:
                print("❗ Invalid date format. Please use YYYY-MM-DD.")

        print("Nutritional Information:")

        # Validate calories
        while True:
            try:
                calories = int(input("  Calories: "))
                if calories < 0:
                    raise ValueError
                break
            except ValueError:
                print("❗ Please enter a non-negative integer for calories.")

         # Validate protein
        while True:
            try:
                protein = int(input("  Protein (grams): "))
                if protein < 0:
                    raise ValueError
                break
            except ValueError:
                print("❗ Please enter a non-negative integer for protein.")

        # Validate fats
        while True:
            try:
                fats = int(input("  Fats: "))
                if fats < 0:
                    raise ValueError
                break
            except ValueError:
                print("❗ Please enter a non-negative integer for fats.")

    # Handle vitamins list
        vits = input("Vitamins it is rich in (separate with commas): ")
        vitamins = [v.strip().upper() for v in vits.split(",") if v.strip()]
        if not vitamins:
            print("⚠️  No vitamins entered. Proceeding with an empty list.")

    # Unique ID check
        while True:
            item_id = input("Enter a unique food item ID to complete: ").strip().upper()
            if not item_id:
                print("❗ Item ID cannot be empty.")
            elif item_id in self.items:
                print("❗ This ID already exists. Please enter a different one.")
            else:
                break

        return item_id, name.upper(), expiry, calories, protein, vitamins, fats, quantity
    


    







