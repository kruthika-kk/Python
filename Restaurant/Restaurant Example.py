# Define the menu of the restaurant
menu = {
    'Pasta': 50,
    'Avocado Toast': 40,
    'Cold Coffee': 35,
    'Pizza': 25,
    'Summer Salad': 45
}

# Greet the customer
print("Welcome to Kruthika's Restaurant!")
print("Here is our menu:")
for item, price in menu.items():
    print(f'{item}: ${price}')

# Function to add item to the order
def add_item_to_order(order_total):
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f'Your item {item} has been added to your order.')
    else:
        print(f'Sorry, {item} is not available on the menu.')
    return order_total

# Creating a variable to keep track of the order total
order_total = 0

# Adding the first item to the order
order_total = add_item_to_order(order_total)

# Ask if the customer wants to add another item
while True:
    another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_item == 'yes':
        order_total = add_item_to_order(order_total)
    elif another_item == 'no':
        break
    else:
        print("Please enter 'Yes' or 'No'.")

# Display the total amount to be paid
print(f'The total amount you have to pay is ${order_total}')
