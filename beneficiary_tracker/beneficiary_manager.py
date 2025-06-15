import json
from .beneficiary import Beneficiary
from tabulate import tabulate

class BeneficiaryManager:
    # initialize the beneficiaries as dictionary
    def __init__(self):
        self.beneficiaries = {}
    
    def add(self, beneficiary):
        self.beneficiaries[beneficiary.id] = beneficiary
    
    # retrieve a beneficiary using its ID
    def get(self, beneficiary_id):
        return self.beneficiaries.get(beneficiary_id)
    
    # retrieve a beneficiary ID, then remove from dictionary
    def remove(self, beneficiary_id):
        if beneficiary_id in self.beneficiaries:
            del self.beneficiaries[beneficiary_id]
    
    # display all beneficiaries in a formatted table using tabulate
    def show_all(self):
        if not self.beneficiaries:
            print("No beneficiaries found.")
        else: 
            table = []
            for beneficiary in self.beneficiaries.values():
                table.append([
                    beneficiary.id,
                    beneficiary.name,
                    beneficiary.contact_info,
                    beneficiary.needs["calories"],
                    beneficiary.needs["protein"],
                    ", ".join(beneficiary.needs["vitamins"])
                ])
            
            headers = ["ID", "Name", "Contact Info", "Required Calories", "Required Protein", "Required Vitamins"]
            print(tabulate(table, headers=headers, tablefmt="grid"), "\n")

    # search for beneficiaries according to user input (any category)
    def search(self, value):
        value = value.lower()
        results = []
        for b in self.beneficiaries.values():
            if (value == b.id.lower() or
                value == b.name.lower() or
                value == b.contact_info.lower() or
                value == str(b.needs["calories"]).lower() or
                value == str(b.needs["protein"]).lower() or
                any(value == v.lower() for v in b.needs["vitamins"])):
                results.append(b)
        
        if not results:
            print(f'No beneficiaries matched the search value {value}.')
            return

        # format results into a table using tabulate
        table = []
        for beneficiary in results:
                table.append([
                    beneficiary.id,
                    beneficiary.name,
                    beneficiary.contact_info,
                    beneficiary.needs["calories"],
                    beneficiary.needs["protein"],
                    ", ".join(beneficiary.needs["vitamins"])
                ])
        
        headers = ["ID", "Name", "Contact Info", "Required Calories", "Required Protein", "Required Vitamins"]
        print(tabulate(table, headers=headers, tablefmt="grid"), "\n")
    
    # save the beneficiary data to a JSON file
    def save_data(self, filename):
        data = {beneficiary_id: beneficiary.to_dict() for beneficiary_id, beneficiary in self.beneficiaries.items()}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    # load beneficiary data from a JSON file. if it doesn't exist, save_data will create a new one.
    def load_data(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for beneficiary_id, beneficiary_data in data.items():
                    self.beneficiaries[beneficiary_id] = Beneficiary.from_dict(beneficiary_data)
        except FileNotFoundError:
            print("Beneficiary file not found. Starting fresh.")
    
    def generate_id(self):
        # if there are no beneficiaries, start from the first ID (B001).
        if not self.beneficiaries:
            return "B001"
        
        # takes the numeric values from the ID (ex. B001 will turn into 1 instead).
        beneficiary_ids = [
            int(b_id[1:]) for b_id in self.beneficiaries.keys() if b_id.startswith("B") and b_id[1:].isdigit()
        ]

        # find the highest existing ID first, then generate the next ID by incrementing max_id by 1
        max_id = max(beneficiary_ids)
        next_id = max_id + 1
        # simple formatting
        return f"B{next_id:03d}"
