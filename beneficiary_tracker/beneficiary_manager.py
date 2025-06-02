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

juan = Beneficiary("001", "Mar Joseph Bijer", "09198868996")
    
# example hash table
# class HashTable:
#     def __init__(self):
#         # Under the hood this is a Python dict
#         self._table = {}

#     def add(self, key, value):
#         """Insert or update the value for this key."""
#         self._table[key] = value

#     def get(self, key):
#         """
#         Retrieve the value for this key.
#         Returns None if the key is not present.
#         """
#         return self._table.get(key)