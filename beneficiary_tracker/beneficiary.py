class Beneficiary:
    # Dietary needs are optional.
    def __init__(self, beneficiary_id, name, contact_info, dietary_needs = None):
        self.id = beneficiary_id
        self.name = name
        self.contact_info = contact_info
        self.dietary_needs = dietary_needs
    
    def __str__(self):
        return f"ID: {self.id}\n Full Name: {self.name}\n Contact Info: {self.contact_info}"