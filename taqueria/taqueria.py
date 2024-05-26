def main():
    # Define the menu and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Initialize the total cost
    total_cost = 0

    try:
        while True:

            # Prompt the user to input an item
            item = input("Item: ")

            # Remove leading/trailing whitespaces
            item = item.strip()

            # Capitalize the first letter of each word
            item = item.title()

            # If the item is found in the menu
            if item in menu:

                # Add its cost to the total_cost variable
                total_cost = total_cost + menu[item]

                # Print the current total cost formatted to two decimal places
                print(f"Total: ${total_cost:.2f}")

            # Otherwise
            else:

                # Inform the user and prompt them to choose from the menu
                print("Invalid item. Please choose from the menu.")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
