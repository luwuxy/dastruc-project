import uuid
import json
from datetime import datetime
from collections import Counter
import heapq
from copy import deepcopy

class Distributor:
    # initialize with access to inventory and beneficiary manager
    def __init__(self, inventory, beneficiary_manager):
        self.inventory = inventory
        self.beneficiary_manager = beneficiary_manager
        self.distribution_tickets = []  # stores tickets after each distribution

    # distribute to all beneficiaries method. automatically match food to each beneficiary's needs and distribute
    def distribute(self):
        tickets_made = 0
        beneficiaries_served = 0

        for beneficiary in self.beneficiary_manager.beneficiaries.values():
            # try to create a food pack that matches this beneficiary's nutritional needs
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
        
        # final summary after all beneficiaries are processed
        print("\n📋 Distribution Summary")
        print("----------------------------")
        print(f"🎟️  Tickets created: {tickets_made}")
        print(f"👥 Beneficiaries served: {beneficiaries_served}")
        print("----------------------------\n")

    # algorithm to match available food to the dietary needs of a single beneficiary
    def match_food_to_needs(self, beneficiary):
        # required nutrients pulled from the beneficiary profile
        req = {
            "fats": beneficiary.needs["fats"],
            "calories": beneficiary.needs["calories"],
            "protein": beneficiary.needs["protein"],
            "vitamins": list(beneficiary.needs["vitamins"])
        }

        # tracker for total nutrients in the current food pack
        total = {"fats": 0, "calories": 0, "protein": 0, "vitamins": set()}
        pack = []  # list of chosen food items

        # helper function: computes a total "error" between required and current nutrients
        def total_error(total):
            errs = []
            for nut in ("fats", "calories", "protein"):
                diff = total[nut] - req[nut]
                errs.append(abs(diff) / req[nut])
            missing = set(req["vitamins"]) - total["vitamins"]
            errs.append(len(missing) / len(req["vitamins"]))
            return sum(errs)

        # current error score before adding anything
        current_err = total_error(total)
        
        heap_copy = deepcopy(self.inventory.expiry_heap)

        # loop: keep adding the best item that reduces the total error
        while True:
            best_item = None
            best_gain = 0.0

            temp_heap = heap_copy[:]

            while temp_heap:
                expiry, item_id = heapq.heappop(temp_heap)
                item = self.inventory.items.get(item_id)

                if not item or item.getQuantity() == 0:
                    continue

                # simulate what happens if we add this item
                sim = total.copy()
                sim["fats"] += item.fats
                sim["calories"] += item.calories
                sim["protein"] += item.protein
                sim["vitamins"] = sim["vitamins"] | set(item.vitamins)

                new_err = total_error(sim)
                gain = current_err - new_err

                # keep track of which item gives the best improvement
                if gain > best_gain:
                    best_gain = gain
                    best_item = item

            # stop if nothing provides any improvement
            if not best_item:
                break

            # commit the selected item
            pack.append(best_item)
            self.inventory.reduce_qty(1, best_item)  # reduce quantity in inventory
            total["fats"] += best_item.fats
            total["calories"] += best_item.calories
            total["protein"] += best_item.protein
            total["vitamins"].update(best_item.vitamins)
            current_err -= best_gain

        # if anything was given, return the food pack and summary
        if pack:
            summary = (
                "\n-----------------------------\n"
                "📦 Total Nutrients Delivered:\n"
                f"- Fats: {total['fats']} / {req['fats']}\n"
                f"- Calories: {total['calories']} / {req['calories']}\n"
                f"- Protein: {total['protein']} / {req['protein']}\n"
                f"- Vitamins: {', '.join(sorted(total['vitamins']))}\n"
                "-----------------------------"
            )
            return pack, summary
        else:
            return None, None

    # allows a user to manually choose food items for a beneficiary
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

        # manual input loop
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

        # only proceed if food pack has contents
        if food_pack:
            # calculate total nutrients
            total = {
                "fats": sum(item.fats for item in food_pack),
                "calories": sum(item.calories for item in food_pack),
                "protein": sum(item.protein for item in food_pack),
                "vitamins": set()
            }
            for item in food_pack:
                total["vitamins"].update(item.vitamins)

            ticket = self.create_ticket(beneficiary_id, food_pack)
            self.distribution_tickets.append(ticket)

            # display final nutrient summary
            print(f"\n✅ Manual distribution complete for {beneficiary.name} (ID: {beneficiary.id})")
            print("\n-----------------------------")
            print("📦 Total Nutrients Delivered:")
            print(f"- Fats: {total['fats']}")
            print(f"- Calories: {total['calories']}")
            print(f"- Protein: {total['protein']}")
            print(f"- Vitamins: {', '.join(sorted(total['vitamins'])) if total['vitamins'] else 'None'}")
            print("-----------------------------")

            self.print_and_export_ticket(ticket)
        else:
            print("⚠️ No items were selected for distribution.")

    # save the distribution ticket as a text file
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
        ticket_lines += [f"- {self.inventory.items[item_id].name} x{count}" for item_id, count in item_counts.items()]
        ticket_text = "\n".join(ticket_lines)

        filename = f"tickets/ticket_{ticket['ticket_id']}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ticket_text + "\n")

    # optionally view ticket, then export to file
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
        ticket_lines += [f"- {self.inventory.items[item_id].name} x{count}" for item_id, count in item_counts.items()]
        ticket_text = "\n".join(ticket_lines)

        # ask user if they want to view ticket now
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

    # generate a dictionary representing a distribution ticket
    def create_ticket(self, beneficiary_id, food_pack):
        return {
            'ticket_id': str(uuid.uuid4())[:8].upper(),  # shortened UUID
            'beneficiary_id': beneficiary_id,
            'food_pack': [item.getID() for item in food_pack],
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
