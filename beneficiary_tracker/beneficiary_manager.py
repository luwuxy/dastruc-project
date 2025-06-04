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
    
    def show(self):
        for beneficiary in self.beneficiaries.values():
            print(beneficiary)

manager = BeneficiaryManager()