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
        return results
