import data
import random


class Product(data.ParentProduct):
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


for x in data.products:
    x["amount"] = random.randrange(x["amount"]["min"], x["amount"]["max"])
    x["price"] = round(random.uniform(x["price"]["min"], x["price"]["max"]), 2)

for x in data.products:
    data.obj_list = data.obj_list + [Product(x["name"], x["amount"], x["price"])]

summary_values_list = [x.calculate_total_value() for x in data.obj_list]

file = open("results_01.txt", "w")
file.writelines(str(summary_values_list))
file.write("\n")
file.writelines(str(data.products))
file.write("\n")
file.writelines(str(data.obj_list))
file.write("\n")
file.close()
