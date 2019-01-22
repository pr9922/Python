class Menu(object):
    """A menu of available items and some associated information.

    This class must have 2 class attributes drink_tax and food_tax
    that are used for the tax amount on drink and food. The value
    should be 0.18 (18%) for drink, and 0.10 (10%) for food.

    """

    drink_tax = .18  #class attributes
    food_tax = .10

    def __init__(self):   ##creating an empty menu
        self.lst = []
    
    def add_item(self, item):
        """Add an item to this menu and set it's menu attribute to this menu.

        Items should not be allowed to be added to more than one menu
        so check if the item is already in another menu.

        """
        if item.menu == None:  ##if not in a menu already
            item.menu=self
            self.lst.append(item)  ##add to this menu      
        


    # TODO: Add a read-only property named items that returns a copy
    # of the set of items in this menu
    @property
    def items(self):
        return self.lst



class Order(object):
    """A list of items that will be purchased together.

    This provides properties that compute prices with tax and tip for
    the whole order.

    """
    def __init__(self):  ##default set order object
        
        self.lst=[]

    
    def add_item(self, item):
        """Add an item to this order.

        Items are required to all be part of one menu. You will need
        to check for this.

        Return True if the item was added, False otherwise (mainly if
        it was not part of the same menu as previous items).

        """
        if len(self.lst) > 0 and self.lst[0].menu != item.menu:   #if list isnt empty and menus dont match
            return False
        else: #lst is empty or there is a match
            self.lst.append(item)
            return True


    def price_plus_tax(self):
        """A computed property that returns the sum of all the item prices
        including their tax.

        """
        price=0
        
        for item in self.lst:          
            price = price + (item.price+(item.price*item._applicable_tax()))

        return price

    
    def price_plus_tax_and_tip(self, amount):
        """A method returns the sum of all the item prices with
        tax and a specified tip.

        amount is given as a proportion of the cost including tax.

        """
        return self.price_plus_tax() + self.price_plus_tax() * amount
    
    
class GroupOrder(Order):
    """An order than is made by a large ground and forces the tip to be at least
    20% (0.20).

    If a price with a tip less than 20% is requested return a price with a 20%
    tip instead.
    """
    def price_plus_tax_and_tip(self, amount):
        
        if amount < .2:
            amount = .2

        return self.price_plus_tax() + self.price_plus_tax() * amount        
    
class Item(object):
    """An item that can be bought.

    It has a name and a price attribute, and can compute its price with
    tax. This also has a menu property that stores the menu this has
    been added to.

    """

    def __init__(self, name, price):
        # TODO: Implement

        self.name = name
        self.price = price
        self.menu1 = None   #default menu setting, renamed to avoid recursion
        self.menuSetOnce = False  #so it can only be set once


    # TODO: Add a property (not just an attribute) called "menu" that
    # returns the menu this item is part of. It should only be
    # possible to set it once.
    @property   
    def menu(self):
        return self.menu1
    
    @menu.setter
    def menu(self,value):
        
        if self.menuSetOnce == False:  #if and ONLY IF menu has not been set once
            self.menu1 = value         #set the order objects menu to value and set it true so it cant be chagned
        self.menuSetOnce = True
    
    def price_plus_tax(self):
        """Return the price of this item with tax added.

        Make sure you could support additional Item types, other than
        what you have in this file (meaning isinstance checks will not
        work). Imagine that I might have a Dessert class that derives
        from Item in another file.

        """       
        return self.price + self._applicable_tax()*self.price
        

    def _applicable_tax(self):
        """Return the amount of tax applicable to this item as a proportion
        (eg. 0.2 if the tax is 20%).
        """
        # This is an abstract method. It should not be implemented in
        # this class.
        raise NotImplementedError


# DO NOT change the classes below. Your code in Item should work with
# these implementation as is.
     
class Food(Item):
    """An Item subclass which uses the food tax rate."""
    def _applicable_tax(self):
        return self.menu.food_tax

class Drink(Item):
    """An Item subclass which uses the drink tax rate."""
    def _applicable_tax(self):
        return self.menu.drink_tax
