buylists = [
    {"task": "buy milk", "done": False},
    {"task": "buy kvarg", "done": True},
    {"task": "buy pants", "done": True}
]
for buylist in buylists:
    print(buylist["task"], "-", buylist["done"])