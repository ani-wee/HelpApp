# Taco Tuesday Ordering System

# Function to print the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito" )
    print("3. Nachos")
    print("4, Soft Drink")
    print("5, Quit")

# Function to get the price of an item
def get_price (selection):
    if selection == 1:
        return 3.50
    elif selection == 2:
        return 5.00
    elif selection == 3:
        return 4.25
    else:
        return 0

# Function to get the item name
def get_item(selection):
    if selection == 1:
        return "Taco"
    elif selection == 2:
        return "Burrito"
    elif selection == 3:
        return "Nachos"
    elif selection == 4:
        return "Soft Drink"
    else:
        return " "

# Main Program
print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection" )

# List to store ordered items
order = [ ]

# Total price starts at zero
total = 0

#Loop until user chooses quit
while True:
    print_menu()

    choice = int(input("\nEnter your selection: "))

    if choice == 5:
        break

    elif choice >= 1 and choice <= 4:
        item = get_item(choice)
        price = get_price(choice)

        print("You selected a", item)

        order.append(item)
        total += price

    else:
        print("Invalid selection. Please choose number from 1-5.")

# Final receipt
    print("\nYour order:")

for item in order:
    print(item)

print("Your total is: $" + format(total, ".2f"))






