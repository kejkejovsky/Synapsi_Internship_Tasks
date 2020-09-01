import random

products = [
    {"name": "Prod1", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod2", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod3", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod4", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod5", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod6", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod7", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod8", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod9", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
    {"name": "Prod10", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
]
obj_list = []

class ParentProduct:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name of this product is {self.name}")

class Product(ParentProduct):
    def __init__(self, name, amount, price):
        super().__init__(name)
        self.amount = amount
        self.price = price

    def show_price(self):
        print(f"{self.name} price is {self.price}")

    def show_amount(self):
        print(f"{self.name} amount is {self.amount}")

    def calculate_total_value(self):
        return round(self.amount * self.price, 2)

for x in products:
    x["amount"] = random.randrange(x["amount"]["min"], x["amount"]["max"])
    x["price"] = round(random.uniform(x["price"]["min"], x["price"]["max"]), 2)

for x in products:
    obj_list = obj_list + [Product(x["name"], x["amount"], x["price"])]

summary_values_list = [x.calculate_total_value() for x in obj_list]

file = open("results_01.txt", "w")
file.writelines(str(summary_values_list))
file.write("\n")
file.writelines(str(products))
file.write("\n")
file.writelines(str(obj_list))
file.write("\n")
file.close()