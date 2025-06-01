food_items_data = [
    # Grains
    {"item_id": "rice1",    "name": "Wellmal Super Fortified Rice", "expiration_date": "2025-12-31", "is_perishable": False, "food_type": "grain"},
    {"item_id": "rice2",    "name": "Dinorado Rice",             "expiration_date": "2025-11-30", "is_perishable": False, "food_type": "grain"},
    {"item_id": "rice3",    "name": "Brown Rice",                "expiration_date": "2025-10-15", "is_perishable": False, "food_type": "grain"},
    
    # Canned goods
    {"item_id": "can1",     "name": "Argentina Corned Beef",      "expiration_date": "2027-01-01", "is_perishable": False, "food_type": "canned"},
    {"item_id": "can2",     "name": "555 Sardines in Tomato Sauce","expiration_date": "2026-03-15", "is_perishable": False, "food_type": "canned"},
    {"item_id": "can3",     "name": "Mega Tuna Flakes",           "expiration_date": "2026-05-20", "is_perishable": False, "food_type": "canned"},
    {"item_id": "can4",     "name": "Century Corned Beef",        "expiration_date": "2027-06-30", "is_perishable": False, "food_type": "canned"},
    
    # Dairy & eggs
    {"item_id": "milk1",    "name": "Alaska Evaporada",           "expiration_date": "2025-07-05", "is_perishable": True,  "food_type": "dairy"},
    {"item_id": "milk2",    "name": "Cowbell Full Cream Milk",    "expiration_date": "2025-06-18", "is_perishable": True,  "food_type": "dairy"},
    {"item_id": "egg1",     "name": "Philippine Fresh Eggs (dozen)","expiration_date": "2025-05-28", "is_perishable": True,  "food_type": "dairy"},
    {"item_id": "yog1",     "name": "Selecta Yogurt Cup",         "expiration_date": "2025-06-10", "is_perishable": True,  "food_type": "dairy"},
    
    # Produce
    {"item_id": "veg1",     "name": "Kangkong (1 bundle)",        "expiration_date": "2025-05-25", "is_perishable": True,  "food_type": "produce"},
    {"item_id": "veg2",     "name": "Talong (5 pcs)",             "expiration_date": "2025-05-26", "is_perishable": True,  "food_type": "produce"},
    {"item_id": "veg3",     "name": "Kamatis (500g)",             "expiration_date": "2025-05-27", "is_perishable": True,  "food_type": "produce"},
    {"item_id": "veg4",     "name": "Patola (1 pc)",              "expiration_date": "2025-05-29", "is_perishable": True,  "food_type": "produce"},
    {"item_id": "fruit1",   "name": "Saba Banana (6 pcs)",        "expiration_date": "2025-06-02", "is_perishable": True,  "food_type": "produce"},
    {"item_id": "fruit2",   "name": "Ripe Mango (3 pcs)",         "expiration_date": "2025-05-30", "is_perishable": True,  "food_type": "produce"},
    {"item_id": "fruit3",   "name": "Pineapple (1 pc)",           "expiration_date": "2025-06-05", "is_perishable": True,  "food_type": "produce"},
    
    # Meat & Fish
    {"item_id": "meat1",    "name": "Chicken Leg Quarter (1kg)",  "expiration_date": "2025-05-24", "is_perishable": True,  "food_type": "meat"},
    {"item_id": "meat2",    "name": "Pork Liempo (1kg)",          "expiration_date": "2025-05-23", "is_perishable": True,  "food_type": "meat"},
    {"item_id": "meat3",    "name": "Beef Tapa Pack (500g)",      "expiration_date": "2025-05-29", "is_perishable": True,  "food_type": "meat"},
    {"item_id": "fish1",    "name": "Bangus (1 pc)",              "expiration_date": "2025-05-22", "is_perishable": True,  "food_type": "fish"},
    {"item_id": "fish2",    "name": "Galunggong (5 pcs)",         "expiration_date": "2025-05-21", "is_perishable": True,  "food_type": "fish"},
    {"item_id": "fish3",    "name": "Dried Daing (200g)",         "expiration_date": "2025-12-31", "is_perishable": False, "food_type": "fish"},
    
    # Condiments & staples
    {"item_id": "cond1",    "name": "Datu Puti Vinegar (500ml)",   "expiration_date": "2027-12-31", "is_perishable": False, "food_type": "condiment"},
    {"item_id": "cond2",    "name": "Silver Swan Soy Sauce (500ml)","expiration_date": "2027-12-31", "is_perishable": False, "food_type": "condiment"},
    {"item_id": "cond3",    "name": "McCormick Ground Pepper",     "expiration_date": "2028-01-01", "is_perishable": False, "food_type": "condiment"},
    {"item_id": "salt1",    "name": "Refined Salt (1kg)",         "expiration_date": "2030-01-01", "is_perishable": False, "food_type": "condiment"},
    {"item_id": "sugar1",   "name": "Refined Sugar (1kg)",        "expiration_date": "2030-01-01", "is_perishable": False, "food_type": "condiment"},
    
    # Beverages & snacks
    {"item_id": "bev1",     "name": "Nescafé Classic (200g)",      "expiration_date": "2027-06-01", "is_perishable": False, "food_type": "beverage"},
    {"item_id": "bev2",     "name": "Lipton Lemon Tea (25 bags)",  "expiration_date": "2026-11-11", "is_perishable": False, "food_type": "beverage"},
    {"item_id": "snack1",   "name": "Oishi Prawn Crackers (70g)",  "expiration_date": "2025-09-01", "is_perishable": False, "food_type": "snack"},
    {"item_id": "snack2",   "name": "SkyFlakes Crackers (80g)",    "expiration_date": "2025-08-15", "is_perishable": False, "food_type": "snack"},
    {"item_id": "snack3",   "name": "Nissin Cup Noodles (Chicken)", "expiration_date": "2025-12-01", "is_perishable": False, "food_type": "snack"},
]

beneficiaries_data = [
    {"beneficiary_id": "ben001", "name": "Maria Santos",      "dietary_needs": ["low-sodium"]},
    {"beneficiary_id": "ben002", "name": "Juan dela Cruz",    "dietary_needs": ["diabetic"]},
    {"beneficiary_id": "ben003", "name": "Ana Reyes",         "dietary_needs": []},
    {"beneficiary_id": "ben004", "name": "Mark Villanueva",   "dietary_needs": ["vegetarian"]},
    {"beneficiary_id": "ben005", "name": "Grace Lim",         "dietary_needs": ["lacto-vegetarian"]},
    {"beneficiary_id": "ben006", "name": "Peter Gonzales",    "dietary_needs": ["low-sugar"]},
    {"beneficiary_id": "ben007", "name": "Liza Pascual",      "dietary_needs": ["gluten-free"]},
    {"beneficiary_id": "ben008", "name": "Enrique Ramos",     "dietary_needs": ["no-pork"]},
    {"beneficiary_id": "ben009", "name": "Cecilia Uy",        "dietary_needs": ["pregnant"]},
    {"beneficiary_id": "ben010", "name": "Ramon Bautista",    "dietary_needs": ["diabetic", "low-sodium"]},
    {"beneficiary_id": "ben011", "name": "Nina Alcantara",    "dietary_needs": []},
    {"beneficiary_id": "ben012", "name": "Ernesto Cruz",      "dietary_needs": ["high-protein"]},
    {"beneficiary_id": "ben013", "name": "Julia Tan",         "dietary_needs": ["vegetarian", "low-sodium"]},
    {"beneficiary_id": "ben014", "name": "Carlos Medina",     "dietary_needs": []},
    {"beneficiary_id": "ben015", "name": "Elena Garcia",      "dietary_needs": ["lactose-intolerant"]},
    {"beneficiary_id": "ben016", "name": "Miguel Lopez",      "dietary_needs": ["low-carb"]},
    {"beneficiary_id": "ben017", "name": "Rosa Santos",       "dietary_needs": ["no-seafood"]},
    {"beneficiary_id": "ben018", "name": "Josefa Reyes",      "dietary_needs": ["vegetarian"]},
    {"beneficiary_id": "ben019", "name": "Andres Villanueva", "dietary_needs": ["diabetic"]},
    {"beneficiary_id": "ben020", "name": "Patricia Lim",      "dietary_needs": ["low-sodium", "low-carb"]},
]
