import json
from .beneficiary import Beneficiary
from tabulate import tabulate

class BeneficiaryManager:
    def __init__(self):
        self.beneficiaries = {}
    
    def add(self, beneficiary):
        self.beneficiaries[beneficiary.id] = beneficiary
    
    def get(self, beneficiary_id):
        return self.beneficiaries.get(beneficiary_id)
    
    def remove(self, beneficiary_id):
        if beneficiary_id in self.beneficiaries:
            del self.beneficiaries[beneficiary_id]
    
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

    def search(self, value):
        value = value.lower()
        results = []
        for b in self.beneficiaries.values():
            if (value in b.id.lower() or
                value in b.name.lower() or
                value in b.contact_info.lower() or
                value in str(b.needs["calories"]).lower() or
                value in str(b.needs["protein"]).lower() or
                any(value in v.lower() for v in b.needs["vitamins"])):
                results.append(b)

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
    
    def save_data(self, filename):
        data = {beneficiary_id: beneficiary.to_dict() for beneficiary_id, beneficiary in self.beneficiaries.items()}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for beneficiary_id, beneficiary_data in data.items():
                    self.beneficiaries[beneficiary_id] = Beneficiary.from_dict(beneficiary_data)
        except FileNotFoundError:
            print("Beneficiary file not found. Starting fresh.")
