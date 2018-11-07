from product import Product

class Inventory:
    def __init__(self):
        '''
        Creates the Inventory object with an empty dictionary and value of 0 for the attributes.
        Inputs: None
        Outputs: None
        '''
        self.inven = {}
        self.value = 0
    def add_item(self,product):
        '''
        Function that adds a product to the Inventory object's dictionary
        Inputs: Product object
        Outputs:None
        '''
        if product.get_id() in self.inven:
            print('Item already exists in the inventory')
        else:
            self.inven[product.get_id()] = product
    def remove_item(self,product_id):
        '''
        Function that removes a product from the Inventory dictionary
        Inputs: product id number 
        Outputs: None
        '''
        del self.inven[product_id]
    def update_item(self, product_id):
        '''
        Function that updates a product's value in the inventory
        Inputs: product id
        Outputs: None
        '''
        if product_id in self.inven:
            value = input('What is the field would you like to update?')
            if 'quantity' in value.lower():
                new_q = input('Enter the new quantity')
                self.inven[product_id].set_quantity(new_q)
            elif 'price' in value.lower():
                new_p = input('Enter the new price')
                self.inven[product_id].set_price(new_p)
            elif 'id' in value.lower():
                new_id = input('Enter the new id')
                self.inven[product_id].set_id(new_id)
            else:
                print('Not at valid input, Item not updated!')
    def get_value_inventory(self):
        '''
        Function that returns the value of the inventory
        Input: None
        Output: Returns the value attribute
        '''
        for id in self.inven:
           self.value += self.inven[id].get_value()  
        return self.value
    def empty_inventory(self):
        '''
        Function that empties the inventory by setting the dictionary to an empty one.
        Input: None
        Output: None
        '''
        self.inven = {}
    def print_inv(self):
        '''
        Function that prints out the contents of the Inventory
        Inputs: None
        Outputs: displays the contents of the Inventory.
        '''
        print("Inventory List:")
        for id in self.inven:
           print(self.inven[id].print_product())
           

    

