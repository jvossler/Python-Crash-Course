"""A class that can be used to represent a restaurant."""

class Restaurant:
    """An attempt to model the attributes of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe a given restaurant."""
        restaurant_description = f"{self.restaurant_name} offers {self.cuisine_type} as a cuisine option."
        # print(restaurant_description)
        return restaurant_description

    def open_restaurant(self):
        """Print a message indicating a restaurant is open for business."""
        restaurant_open = f"{self.restaurant_name} is open for business!"
        # print(restaurant_open)
        return restaurant_open
    
    def set_number_served(self, customer_number):
        """Print the number of customers currently served."""
        number_served = f"You have currently served {customer_number} customers."
        # print(number_served)
        return number_served
    
    def increment_number_served(self, customer_number):
        if customer_number >= 0:
            self.number_served += customer_number
            incremented_number_served = f"You have now served {self.number_served} customers."
            # print(incremented_number_served)
            return incremented_number_served
        else:
            cannot_subtract_number_served = f"You can't subtract from the current number of customers served!"
            # print(cannot_subtract_number_served)
            return cannot_subtract_number_served

class IceCreamStand(Restaurant):
    """An attempt to model the attributes of an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize ice cream stand attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = []
    
    def pick_flavors(self):
        """Pick the flavors of ice cream."""
        if self.flavors == '':
            print("You did not select any flavors of ice cream!")
        else:
            print("\nYou picked the following flavors:")
            for flavor in self.flavors:
                print(f"- {flavor.title()}")