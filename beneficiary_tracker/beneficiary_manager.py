import json
from .beneficiary import Beneficiary

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
            for beneficiary in self.beneficiaries.values():
                print(beneficiary, "\n")

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
        return 
    
    def save_data(self, filename):
        data = {bid: b.to_dict() for bid, b in self.beneficiaries.items()}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for bid, b_data in data.items():
                    self.beneficiaries[bid] = Beneficiary.from_dict(b_data)
        except FileNotFoundError:
            print("Beneficiary file not found. Starting fresh.")
