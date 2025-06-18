class Beneficiary:
    def __init__(self, beneficiary_id, name, contact_info, needs):
        self.id = beneficiary_id
        self.name = name
        self.__contact_info = contact_info  # made private
        self.needs = {
            "fats": needs["fats"],
            "calories": needs["calories"],
            "protein": needs["protein"],
            "vitamins": needs["vitamins"]
        }

    def get_contact_info(self):
        return self.__contact_info

    def get_needs(self):
        return self.needs

    def to_dict(self):
        return {
            "beneficiary_id": self.id,
            "name": self.name,
            "contact_info": self.__contact_info,
            "dietary_needs": self.needs
        }

    @staticmethod
    def from_dict(data):
        return Beneficiary(
            data["beneficiary_id"],
            data["name"],
            data["contact_info"],
            data["dietary_needs"],
        )

    def __str__(self):
        return (f"Beneficiary ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Contact Info: {self.__contact_info}\n"
                f"Dietary Needs:\n"
                f"- Fats: {self.needs['fats']}\n"
                f"- Calories: {self.needs['calories']}\n"
                f"- Protein: {self.needs['protein']}\n"
                f"- Vitamins: {', '.join(self.needs['vitamins'])}")
