import uuid
import json
from datetime import datetime
from collections import Counter

class Distributor:
    def __init__(self, inventory, beneficiary_manager):
        self.inventory = inventory
        self.beneficiary_manager = beneficiary_manager
        self.distribution_tickets = []

    def distribute(self):
        tickets_made = 0
        beneficiaries_served = 0

        for beneficiary in self.beneficiary_manager.beneficiaries.values():
            food_pack, summary = self.match_food_to_needs(beneficiary)
            if food_pack:
                ticket = self.create_ticket(beneficiary.id, food_pack)
                self.distribution_tickets.append(ticket)
                self.save_ticket_to_file(ticket)
                print(summary)
                beneficiaries_served += 1
                tickets_made += 1
            else:
                print(f"❌ Not enough food to match needs for {beneficiary.name}")
        
        print("\n📋 Distribution Summary")
        print("----------------------------")
        print(f"🎟️  Tickets created: {tickets_made}")
        print(f"👥 Beneficiaries served: {beneficiaries_served}")
        print("----------------------------\n")

    def match_food_to_needs(self, beneficiary):
        required = beneficiary.needs.copy()
        food_pack = []
        summary = []

        total = {
            "fats": 0,
            "calories": 0,
            "protein": 0,
            "vitamins": set()
        }

        sorted_items = sorted(self.inventory.items.values(), key=lambda i: i.expiry)

        for item in sorted_items:
            if item.getQuantity() <= 0:
                continue

            units_used = 0

            while item.getQuantity() > 0:
                helps = False

                if total["fats"] < required["fats"] and item.fats > 0:
                    total["fats"] += item.fats
                    helps = True

                if total["calories"] < required["calories"] and item.calories > 0:
                    total["calories"] += item.calories
                    helps = True

                if total["protein"] < required["protein"] and item.protein > 0:
                    total["protein"] += item.protein
                    helps = True

                if not all(v in total["vitamins"] for v in required["vitamins"]):
                    new_vits = set(item.vitamins) - total["vitamins"]
                    if new_vits:
                        total["vitamins"].update(new_vits)
                        helps = True

                if helps:
                    food_pack.append(item)
                    self.inventory.reduce_qty(1, item)
                    units_used += 1
                else:
                    break 

                if (
                    total["fats"] >= required["fats"] and
                    total["calories"] >= required["calories"] and
                    total["protein"] >= required["protein"] and
                    all(v in total["vitamins"] for v in required["vitamins"])
                ):
                    break

            if units_used > 0:
                summary.append(f"{item.name} x{units_used}")

            # stop early if everything's already met
            if (
                total["fats"] >= required["fats"] and
                total["calories"] >= required["calories"] and
                total["protein"] >= required["protein"] and
                all(v in total["vitamins"] for v in required["vitamins"])
            ):
                break

        if (
            total["fats"] >= required["fats"] or
            total["calories"] >= required["calories"] or
            total["protein"] >= required["protein"] or
            any(v in total["vitamins"] for v in required["vitamins"])
        ):
            nutrient_summary = (
                "\n-----------------------------\n"
                "📦 Total Nutrients Delivered:\n"
                f"- Fats: {total['fats']} / {required['fats']}\n"
                f"- Calories: {total['calories']} / {required['calories']}\n"
                f"- Protein: {total['protein']} / {required['protein']}\n"
                f"- Vitamins: {', '.join(sorted(total['vitamins']))}\n"
                "-----------------------------"
            )

            return food_pack, "\n".join(summary) + nutrient_summary
        else:
            return None, None
        
    def manual_distribute(self):
        beneficiary_id = input("Enter the Beneficiary ID: ").strip()
        beneficiary = self.beneficiary_manager.get(beneficiary_id)

        if not beneficiary:
            print("❌ Beneficiary not found.\n")
            return

        food_pack = []

        print("\n📦 Available Food Items:")
        self.inventory.display_inventory()


        print("\nEnter food item IDs and quantities to add to the food pack. Leave ID empty to finish.")

        while True:
            item_id = input("Item ID (or press enter to finish): ").strip()
            if item_id == "":
                break

            item = self.inventory.items.get(item_id)
            if not item:
                print("❌ Item not found.")
                continue

            try:
                qty = int(input(f"How many of {item.name}? (Available: {item.getQuantity()}): ").strip())
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue

            if qty <= 0 or qty > item.getQuantity():
                print("❌ Invalid quantity.")
                continue

            for _ in range(qty):
                food_pack.append(item)
                self.inventory.reduce_qty(1, item)

        if food_pack:
            ticket = self.create_ticket(beneficiary_id, food_pack)
            self.distribution_tickets.append(ticket)
            print(f"\n✅ Manual distribution complete for {beneficiary.name} (ID: {beneficiary.id})")
            self.print_and_export_ticket(ticket)
        else:
            print("⚠️ No items were selected for distribution.")

    def save_ticket_to_file(self, ticket):
        item_counts = Counter(ticket['food_pack'])

        ticket_lines = [
            "\n🧾 Distribution Ticket",
            "-----------------------------",
            f"Ticket ID: {ticket['ticket_id']}",
            f"Beneficiary ID: {ticket['beneficiary_id']}",
            f"Date: {ticket['date']}",
            "Food Pack Contents:"
        ]
        ticket_lines += [f"- {item_id} x{count}" for item_id, count in item_counts.items()]
        ticket_text = "\n".join(ticket_lines)

        filename = f"tickets/ticket_{ticket['ticket_id']}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ticket_text + "\n")


    def print_and_export_ticket(self, ticket):
        item_counts = Counter(ticket['food_pack'])

        ticket_lines = [
            "\n🧾 Distribution Ticket",
            "-----------------------------",
            f"Ticket ID: {ticket['ticket_id']}",
            f"Beneficiary ID: {ticket['beneficiary_id']}",
            f"Date: {ticket['date']}",
            "Food Pack Contents:"
        ]
        ticket_lines += [f"- {item_id} x{count}" for item_id, count in item_counts.items()]
        ticket_text = "\n".join(ticket_lines)

        view = input("Do you want to view the distribution ticket now? (yes/no): ").strip().lower()
        if view in ("yes", "y"):
            while True:
                print(ticket_text)
                option = input("Press enter to continue.")

                if option == "":
                    break

        filename = f"tickets/ticket_{ticket['ticket_id']}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ticket_text + "\n")

        print(f"\n📁 Ticket saved to '{filename}'\n")

    def create_ticket(self, beneficiary_id, food_pack):
        return {
            'ticket_id': str(uuid.uuid4())[:8].upper(),
            'beneficiary_id': beneficiary_id,
            'food_pack': [item.getID() for item in food_pack],
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
