class Beneficiary:
    def __init__(self, beneficiary_id, name, contact_info, needs):
        self.id = beneficiary_id
        self.name = name
        self.contact_info = contact_info
        self.needs = {
            "calories": needs["calories"],
            "protein": needs["protein"],
            "vitamins": needs["vitamins"]
        }

    def __str__(self):
        return (f"Beneficiary ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Contact Info: {self.contact_info}\n"
                f"Dietary Needs:\n"
                f"- Calories: {self.needs["calories"]}\n"
                f"- Protein: {self.needs["protein"]}\n"
                f"- Vitamins: {", ".join(self.needs["vitamins"])}")