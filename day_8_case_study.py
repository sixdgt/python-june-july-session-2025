# Grocery Store Billing System

# stocked products
products = {
    'apple' : {'price': 120.00, 'stock': 15}, # apple details
    'bread' : {'price': 100.00, 'stock': 10}, # bread details
    'banana' : {'price': 150.00, 'stock': 5}, # banana details
    'milk' : {'price': 50.00, 'stock': 10}, # milk details
    'mango' : {'price': 130.00, 'stock': 12}, # mango details
    'xtreme' : {'price': 185.00, 'stock': 30} # xtreme details
}
# cart
cart = {} # empty cart because when the program is executed for the first time not products are added

# Lambda function to calculate 10% discount on totals >= 500
get_discount = lambda total: total * 0.10 if total >= 500 else 0

# def get_discount(total):
#     if total >= 500:
#         return total * 0.10
#     else:
#         return 0

# view products
def view_products():
    """
    This function displays the dictionaries of products available
    """
    print("\nAvailable Products:") # here \n creates new line
    for name, data in products.items():
        print(f"Product: {name.capitalize()} - Price: Rs. {data.get('price')} - Stock: {data.get('stock')}")

# add to cart
def add_to_cart():
    """
    This function stores the products that are added in the cart
    """
    item = input("Enter product name to add: ").lower() # getting product name from user input
    if item in products: # checking if the product is available
        quantity = int(input("Enter quantity: ")) # asking total number of quantity to add
        if quantity <= products.get(item).get('stock'): # checking quantity lesser than stock
            if item in cart: # checking if the item already exists in the cart so that to append the quantity
                cart[item] += quantity
            else:
                cart[item] = quantity # adding item and quantity to cart
            products[item]['stock'] -= quantity # is equivalent to products.get(item).get('stock')
            # after adding the product in cart the stock must be decrease so here the quantity added is decreased from stock
            print(f"{quantity} {item}(s) added to cart.")
        else:
            print("Insufficient stock.")
    else:
        print("Product not found.")

cart = {
    'banana': 2,
    'milk': 5
}
# remove from cart
def remove_from_cart():
    """
    This function removes the product from the cart
    """
    item = input("Enter product name: ").lower()
    if item in cart:
        quantity = int(input("Enter quantity to remove: "))
        if quantity >= cart[item]: # cart['banana']
            products[item]['stock'] += cart[item] # adding the stock again since the item is removed from cart
            del cart[item] # cart.pop(item)
        else:
            cart[item] -= quantity # incase of removing quantity lesser than available in the cart
            products[item]['stock'] += quantity
        print(f"{item} removed from cart.")
    else:
        print("Item not in cart.")

# view cart
def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\n--------- Cart ---------")
    total = 0
    for item, quantity in cart.items():
        price = products[item]['price'] * quantity # calculating price of item i.e product based on quantity
        print(f"Product: {item.capitalize()} x {quantity} = Rs. {price}")
        total += price # calculating the total price of all item
    print(f"Total: Rs. {total}")

# checkout
def checkout():
    if not cart:
        print("Cart is empty.")
        return
    print("\n--------- Checkout ---------")
    total = sum(products[item]['price'] * quantity for item, quantity in cart.items())
    unique_items = set(cart.keys())
    discount = get_discount(total)
    if len(unique_items) > 3:
        discount += total * 0.05 # extra 5% discount for unique items or products more than 3
    final_total = total - discount
    print("Receipt:")
    for item, quantity in cart.items():
        print(f"{item.capitalize()} x {quantity} = Rs.{products[item]['price'] * quantity}")
    print(f"Subtotal: Rs. {total}")
    print(f"Discount: Rs. {discount:.2f}") # .2f means it takes only 2 digits after decimal
    print(f"Total Payable: Rs.{final_total:.2f}")
    cart.clear()

# main method to execute the program

def main():
    while True:
        print("\n--------- Grocery Billing System ----------")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        feature = input("Enter from number 1 to 6 to use the features: ")
        if feature == '1':
            view_products()
        elif feature == '2':
            add_to_cart()
        elif feature == '3':
            remove_from_cart()
        elif feature == '4':
            view_cart()
        elif feature == '5':
            checkout()
        elif feature == '6':
            print("Thank you for using Grocery Billing System")
            break
        else:
            print("Invalid feature. Try again.")

if __name__ == "__main__": # it will directly run the python script
    main()