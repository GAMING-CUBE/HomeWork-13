products = {
    1: {"Name": "Core-i3-4330", "Amount": 9, "Price": 4500},
    2: {"Name": "Core i5-4670K", "Amount": 3, "Price": 8500},
    3: {"Name": "AMD FX-6300", "Amount": 6, "Price": 3700},
    4: {"Name": "Pentium G3220", "Amount": 8, "Price": 2100},
    5: {"Name": "Core i5-3450", "Amount": 5, "Price": 6400}
}

for product_id, product_info in products.items():
    print(product_id, product_info["Name"], product_info["Amount"], product_info["Price"])

while True:
    input_id = int(input())
    if input_id == 0:
        break
    elif input_id in products:
        new_quantity = int(input())
        products[input_id]["Amount"] = new_quantity

print("ID", "Name", "Amount", "Price")
for product_id, product_info in products.items():
    print(product_id, product_info["Name"], product_info["Amount"], product_info["Price"])
