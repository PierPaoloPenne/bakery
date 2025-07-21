# Sweet Surrender Bakery Inventory Management System
# A simple but effective tool for tracking ingredient inventory

# Global dictionary to store all ingredient information
ingredients = {}

def display_welcome():
    """Display a friendly welcome message when the program starts"""
    print("\n" + "="*50)
    print("Welcome to Sweet Surrender Bakery Inventory System!")
    print("="*50)
    print("This system will help you track your ingredient inventory")
    print("easily and reliably. Let's get started!\n")

def display_menu():
    """Show the main menu options clearly"""
    print("="*50)
    print("Sweet Surrender Bakery - Inventory System")
    print("="*50)
    print("1. Add New Ingredient")
    print("2. View All Ingredients")
    print("3. Search for Ingredient")
    print("4. Update Ingredient Quantity")
    print("5. Exit")
    print("="*50)

def add_ingredient():
    """Add a new ingredient to the inventory system"""
    print("\n--- Add New Ingredient ---")
    
    # Get ingredient name with validation
    name = input("Enter ingredient name: ").strip()
    if not name:
        print("Error: Ingredient name cannot be empty!")
        return
    
    # Check if ingredient already exists
    if name.lower() in [existing_name.lower() for existing_name in ingredients.keys()]:
        print(f"Ingredient '{name}' already exists in inventory!")
        choice = input("Would you like to update its quantity instead? (y/n): ").lower()
        if choice == 'y':
            update_ingredient()
            return
        else:
            return
    
    # Get quantity with validation
    try:
        quantity = float(input("Enter quantity: "))
        if quantity <= 0:
            print("Error: Quantity must be positive!")
            return
    except ValueError:
        print("Error: Please enter a valid number for quantity!")
        return
    
    # Get unit of measurement
    unit = input("Enter unit (kg, litres, pieces, etc.): ").strip()
    if not unit:
        print("Error: Unit cannot be empty!")
        return
    
    # Store the ingredient in our database
    ingredients[name] = {"quantity": quantity, "unit": unit}
    print(f"✓ Added: {name.title()} - {quantity} {unit}")

def view_all_ingredients():
    """Display all ingredients in a nice, organized table"""
    print("\n--- Current Inventory ---")
    
    if not ingredients:
        print("No ingredients in inventory yet.")
        print("Use option 1 to add some ingredients!")
        return
    
    # Create a formatted table header
    print("-" * 60)
    print(f"{'Ingredient':<20} {'Quantity':<15} {'Unit':<10}")
    print("-" * 60)
    
    # Display each ingredient in a formatted row
    for name, details in ingredients.items():
        print(f"{name.title():<20} {details['quantity']:<15} {details['unit']:<10}")
    
    print("-" * 60)
    print(f"Total ingredients in inventory: {len(ingredients)}")

def search_ingredient():
    """Search for a specific ingredient by name"""
    print("\n--- Search for Ingredient ---")
    
    if not ingredients:
        print("No ingredients in inventory to search through.")
        return
    
    search_term = input("Enter ingredient name to search for: ").strip().lower()
    if not search_term:
        print("Error: Please enter a search term!")
        return
    
    # Look for ingredients that match the search term
    found_ingredients = []
    for name, details in ingredients.items():
        if search_term in name.lower():
            found_ingredients.append((name, details))
    
    # Display results
    if found_ingredients:
        print(f"\n--- Search Results for '{search_term}' ---")
        print("-" * 50)
        for name, details in found_ingredients:
            print(f"Found: {name.title()}")
            print(f"Quantity: {details['quantity']} {details['unit']}")
            print("-" * 50)
    else:
        print(f"No ingredients found matching '{search_term}'")
        print("Try checking your spelling or searching for part of the name.")

def update_ingredient():
    """Update the quantity of an existing ingredient"""
    print("\n--- Update Ingredient Quantity ---")
    
    if not ingredients:
        print("No ingredients in inventory to update.")
        return
    
    # Get the ingredient name to update
    name_to_update = input("Enter name of ingredient to update: ").strip()
    if not name_to_update:
        print("Error: Please enter an ingredient name!")
        return
    
    # Find the ingredient (case-insensitive search)
    actual_name = None
    for existing_name in ingredients.keys():
        if existing_name.lower() == name_to_update.lower():
            actual_name = existing_name
            break
    
    if not actual_name:
        print(f"Error: Ingredient '{name_to_update}' not found in inventory!")
        print("Use option 3 to search for ingredients, or option 2 to view all.")
        return
    
    # Show current quantity
    current_quantity = ingredients[actual_name]['quantity']
    current_unit = ingredients[actual_name]['unit']
    print(f"Current quantity of {actual_name.title()}: {current_quantity} {current_unit}")
    
    # Get new quantity
    try:
        new_quantity = float(input("Enter new quantity: "))
        if new_quantity < 0:
            print("Error: Quantity cannot be negative!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    # Update the ingredient
    old_quantity = ingredients[actual_name]['quantity']
    ingredients[actual_name]['quantity'] = new_quantity
    
    print(f"✓ Updated {actual_name.title()}: {old_quantity} → {new_quantity} {current_unit}")

def main():
    """Main program function that runs everything"""
    display_welcome()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_ingredient()
        elif choice == '2':
            view_all_ingredients()
        elif choice == '3':
            search_ingredient()
        elif choice == '4':
            update_ingredient()
        elif choice == '5':
            print("\n" + "="*40)
            print("Thank you for using Sweet Surrender")
            print("Bakery Inventory System!")
            print("Have a wonderful day of baking!")
            print("="*40)
            break
        else:
            print("Error: Please enter a number between 1 and 5.")
        
        # Pause
        input("\nPress Enter to continue...")

# Start the program
if __name__ == "__main__":
    main()
