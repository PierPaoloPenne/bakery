"""
Sweet Surrender Bakery - Simple Ingredient Inventory Management System
A basic Python program to help manage bakery ingredient inventory using dictionaries
"""

# Simple dictionary to store ingredients - no file saving needed for this basic version
ingredients = {}

def add_ingredient():
    """Add a new ingredient to the inventory"""
    print("\n--- Add New Ingredient ---")
    
    # Get ingredient name
    name = input("Enter ingredient name: ").strip().lower()
    if not name:
        print("Error: Ingredient name cannot be empty!")
        return
    
    # Get quantity
    try:
        quantity = float(input("Enter quantity: "))
        if quantity <= 0:
            print("Error: Quantity must be positive!")
            return
    except ValueError:
        print("Error: Please enter a valid number for quantity!")
        return
    
    # Get unit
    unit = input("Enter unit (kg, litres, pieces, etc.): ").strip()
    if not unit:
        print("Error: Unit cannot be empty!")
        return
    
    # Add to dictionary
    ingredients[name] = {'quantity': quantity, 'unit': unit}
    print(f"✓ Added: {name.title()} - {quantity} {unit}")

def view_all_ingredients():
    """Display all ingredients in the inventory"""
    print("\n--- All Ingredients ---")
    
    if not ingredients:
        print("No ingredients in inventory yet.")
        return
    
    print(f"{'Ingredient':<15} {'Quantity':<10} {'Unit'}")
    print("-" * 35)
    
    # Loop through dictionary and display each ingredient
    for name, details in ingredients.items():
        print(f"{name.title():<15} {details['quantity']:<10} {details['unit']}")

def search_ingredient():
    """Search for a specific ingredient"""
    print("\n--- Search Ingredient ---")
    
    name = input("Enter ingredient name to search: ").strip().lower()
    if not name:
        print("Error: Please enter an ingredient name!")
        return
    
    # Check if ingredient exists in dictionary
    if name in ingredients:
        ingredient = ingredients[name]
        print(f"Found: {name.title()}")
        print(f"Quantity: {ingredient['quantity']} {ingredient['unit']}")
    else:
        print(f"Ingredient '{name}' not found in inventory.")

def update_ingredient():
    """Update the quantity of an existing ingredient"""
    print("\n--- Update Ingredient Quantity ---")
    
    name = input("Enter ingredient name to update: ").strip().lower()
    if not name:
        print("Error: Please enter an ingredient name!")
        return
    
    # Check if ingredient exists
    if name not in ingredients:
        print(f"Ingredient '{name}' not found in inventory.")
        return
    
    # Get new quantity
    try:
        new_quantity = float(input("Enter new quantity: "))
        if new_quantity < 0:
            print("Error: Quantity cannot be negative!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    # Update the quantity
    old_quantity = ingredients[name]['quantity']
    ingredients[name]['quantity'] = new_quantity
    
    print(f"✓ Updated {name.title()}: {old_quantity} → {new_quantity} {ingredients[name]['unit']}")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("Sweet Surrender Bakery - Inventory System")
    print("="*40)
    print("1. Add New Ingredient")
    print("2. View All Ingredients") 
    print("3. Search for Ingredient")
    print("4. Update Ingredient Quantity")
    print("5. Exit")
    print("="*40)

def main():
    """Main program that runs the inventory system"""
    print("Welcome to Sweet Surrender Bakery Inventory System!")
    
    # Main program loop
    while True:
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice (1-5): ").strip()
        
        # Handle each menu option using if-elif statements
        if choice == '1':
            add_ingredient()
        elif choice == '2':
            view_all_ingredients()
        elif choice == '3':
            search_ingredient()
        elif choice == '4':
            update_ingredient()
        elif choice == '5':
            print("Thank you for using the inventory system!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        # Wait before showing menu again
        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()