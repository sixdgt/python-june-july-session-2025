cosmetics = {
    "lipstick": {"brand": "Luxe","color": "Red Velvet","price": 19.99,"in_stock": True},
    "eyeshadow": {"brand": "Glamour","color": "Smoky Grey","price": 24.99,"in_stock": False},
    "mascara": {"brand": "Bold Lash","color": "Black","price": 15.99,"in_stock": True}
}

fruits = {
    "apple": {"price": 0.5, "stock": 100},
    "banana": {"price": 0.3, "stock": 150},
    "orange": {"price": 0.8, "stock": 80}
}

category = input("Enter category: 1. Cosmetics 2. Fruits: ").lower()
if category == "1":
    for item, details in cosmetics.items():
        print(f"{item.capitalize()} Brand: {details['brand']} Color: {details.get('color')}")
elif category == "2":
    for item, details in fruits.items():
        print(f"{item.capitalize()} Price: ${details['price']} Stock: {details.get('stock')}")