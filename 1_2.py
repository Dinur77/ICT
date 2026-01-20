def add_product(products, name, price):
    # Add a new product to the dictionary with name as key and price as value
    products[name] = price
    print("Product added.")

def remove_product(products, name):
    # Check if the product exists in the dictionary
    if name in products:
        # Remove the product from the dictionary
        del products[name]
        print("Product removed.")
    else:
        # Inform user if product was not found
        print("Product not found.")

def view_products(products):
    # Loop through all products in the dictionary
    for name, price in products.items():
        # Display each product name and its price
        print(f"{name}: {price}")

def main():
    # Create an empty dictionary to store products
    products = {}
    
    # Main program loop - runs until user chooses to quit
    while True:
        # Get user action and normalize input (strip whitespace, convert to lowercase)
        action = input("Choose action: add, remove, view, quit\n> ")
        
        # Handle "add" action
        if action == "add":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            add_product(products, name, price)
        
        # Handle "remove" action  
        elif action == "remove":
            name = input("Enter product name to remove: ")
            remove_product(products, name)
        
        # Handle "view" action
        elif action == "view":
            view_products(products)
        
        # Handle "quit" action - break out of the loop
        elif action == "quit":
            break
        
        # Handle invalid input
        else:
            print("Invalid action.")

# Standard Python practice - only run main() if this file is executed directly
if __name__ == "__main__":
    main()