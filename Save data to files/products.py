import json

with open("products.json", "r") as file:
    products = json.load(file)

cheapest = min(products, key=lambda p: p["price"])
expensive = max(products, key=lambda p: p["price"])

print("\nCheapest product:", cheapest["product"], ":", cheapest["price"])
print("\nMost expensive product:", expensive["product"], ":", expensive["price"])

for product in products:
    if product["price"] < 100:
        print("- ", product["product"], ":", product["price"])