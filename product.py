class Product:
    def __init__(self, idnum, price, quantity):
        '''
        Creates a Product object with the attributes idnum, price and quantitiy.
        Inputs: idnum, price and quantity.
        Outputs: None
        '''
        self.idnum = idnum
        self.price = price
        self.quantity = quantity

    def get_id(self):
        '''
        Function that returns the idnum attribute
        Inputs: None
        Outputs: returns the idnum.
        '''
        return self.idnum
    def get_price(self):
        '''
        Function that returns the price attribute
        Inputs: None
        Outputs: returns the price
        '''
        return self.price
    def get_quantity(self):
        '''
        Function that returns the quantity attributes
        Inputs: NOne
        Outputs: returns the quantity
        '''
        return self.quantity
    def set_id(self, newid):
        '''
        Function that sets the idnum attribute to a new value.
        Inputs: newid number 
        Outputs: None
        '''
        self.idnum = newid
    def set_price(self,price):
        '''
        Function that sets a new price for a product 
        Inputs: price
        Outputs: None
        '''
        self.price = price
    def set_quantity(self,quantity):
        '''
        Function that sets a new quantity
        Inputs: a new quantity
        Outputs: None
        '''
        self.quantity = quantity
    def get_value(self):
        '''
        Function that returns the value of the object
        Inputs: None
        Outputs: value of the object (price * quantity)
        '''
        return self.price * self.quantity
    def __str__(self):
        '''
        Function that returns a listing of the product for any calls that expect a string returned
        Inputs: None
        Outputs: Returns a string listing of the product.
        '''
        string = 'id:'
        string = str(self.idnum) + ' quantity:' + str(self.quantity) + ' price:' + str(self.price)
        return string
    def print_product(self):
        '''
        Function that returns a listing of the product
        Inputs: None
        Outputs: Returns a string listing of the product
        '''
        string = 'id:'
        string = string + str(self.idnum) + ' quantity:' + str(self.quantity) + ' price:' + str(self.price)
        return string
    


