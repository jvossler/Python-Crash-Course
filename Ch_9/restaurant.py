class Restaurant:
    """Create a model for a restaurant and its attributes."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} offers {self.cuisine_type} as a cuisine option.")

    
    def open_restaurant(self):
        """Print a message indicating a restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")
    
    def set_number_served(self, customer_number):
        """Return the number of customers currently served."""
        print(f"You have currenly served {customer_number} customers.")

    def increment_number_served(self, customer_number):
        """Increment the number of customers served in any given timeframe."""
        if customer_number >= 0:
            self.number_served += customer_number
            print(f"You have now served {self.number_served} customers.")
        else:
            print("You can't subtract from the current number of customers served!")


# Add a method called set_number_served() that 
# lets you set the number of customers that have 
# been served. Call this method with a new number 
# and print the value again.

# Add a method called increment_number_served() 
# that lets you increment the number of customers 
# who’ve been served. Call this method with any 
# num-ber you like that could represent how many 
# customers were served in, say, a day of business.