from inventory import Inventory
from product import Product

def display_menu():
    '''
    Diplay function that shows the menu to the user
    Inputs: none
    Outputs: menu displayed to the terminal
    '''
    print('''
    Inventory Program
    ______________________________
    1. Add a new product
    2. Remove an item
    3. Delete an inventory 
    4. Display the Inventory
    5. Get Inventory value
    6. Update value in inventory
    7. Quit
    ''')

def manage_inventory(inv):
    '''
    Function that manages the choices of the user from the menu
    Inputs: Inventory object
    Outputs: None
    '''
    end = False
    while end == False:
        display_menu()
        choice = input()
        if choice == '1' or 'add' in choice.lower():
            idnum = int(input('Enter the id number:'))
            price = float(input('Enter the price:'))
            quantity = int(input('Enter the quantity:'))
            add_product = Product(idnum,price,quantity)
            inv.add_item(add_product)
        elif choice == '2' or 'delete' in choice.lower():
            delnum = int(input('Enter the ID of the number you want to delete:'))
            inv.remove_item(delnum)
        elif choice == '3' or 'remove' in choice.lower():
            inv.empty_inventory()
        elif choice == '4' or 'display' in choice.lower():
            inv.print_inv()
        elif choice == '5' or 'get' in choice.lower():
            print(f'The inventory is valued at:{inv.get_value_inventory()}')
        elif choice == '6' or 'update' in choice.lower():
            update_value = int(input('What is the id of the item, you wish to change?'))
            inv.update_item(update_value)
        elif choice == '7' or 'quit' in choice.lower():
            end = True
            print('Program quiting')
        else: 
            print('Error please enter a valud choice')

inv = Inventory()
manage_inventory(inv)








