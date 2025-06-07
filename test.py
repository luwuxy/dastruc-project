from beneficiary_tracker.beneficiary import Beneficiary
from beneficiary_tracker.beneficiary_manager import BeneficiaryManager

manager = BeneficiaryManager()

needs = {
    "calories": 1800,
    "protein": 60,
    "vitamins": ["A", "B12"]
}

beneficiary = Beneficiary("B001", "User One", "example@gmail.com", needs)
beneficiary2 = Beneficiary("B002", "User Two", "example2@gmail.com", needs)

manager.add(beneficiary)
manager.add(beneficiary2)

print("Listing all beneficiaries:\n")
manager.show_all()

print("Printing individual beneficiary:\n")
print(manager.get("B001"))