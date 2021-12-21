from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """A class about an ice cream stand's attributes."""

    def __init__(self, flavors):
        """Initialize ice cream stand class."""
        self.flavors = flavors

    def pick_flavors(self):
        """Pick the flavor of ice cream."""
        ice_cream_flavors = []
        # flavor = input("Which ice cream flavor did you get?")
        ice_cream_flavors.append(self.flavors)
        print(f"You picked the {self.flavors} flavor of ice cream.")