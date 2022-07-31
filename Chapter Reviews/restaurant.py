"""A set of classes used to represent restaurants."""

class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.name} is now open!")
    
    def customers_served(self):
        """Print the number of customers served."""
        print(f"We have served {self.number_served} customers.")
    
    def set_number_served(self, customers):
        """Set the number of customers served."""
        self.number_served = customers
    
    def increment_number_served(self, customers):
        """Add the given amount to the number of customers served."""
        if customers >= 0:
            self.number_served += customers
        else:
            print("Please provide a positive number of customers.")
            
# class IceCreamStand(Restaurant):
#     """A simple attempt to model an ice cream stand."""
    
#     def __init__(self, name, cuisine_type):
#         """Initialize attributes of the parent class."""
#         super().__init__(name, cuisine_type)
#         self.flavors = ['vanilla', 'chocolate', 'strawberry']
        
#     def display_flavors(self):
#         """Display the flavors available."""
#         print(f"We have the following flavors available:")
#         print(*self.flavors, sep='\n')
#         # flavors = [flavor for flavor in {self.flavors}]
#         # print(flavors)
#         # for flavor in self.flavors:
#         #     print(flavor)
        

# from restaurant import Restaurant

# class IceCreamStand(Restaurant):
#     """A class about an ice cream stand's attributes."""

#     def __init__(self, flavors):
#         """Initialize ice cream stand class."""
#         self.flavors = flavors

#     def pick_flavors(self):
#         """Pick the flavor of ice cream."""
#         ice_cream_flavors = []
#         # flavor = input("Which ice cream flavor did you get?")
#         ice_cream_flavors.append(self.flavors)
#         print(f"You picked the {self.flavors} flavor of ice cream.")