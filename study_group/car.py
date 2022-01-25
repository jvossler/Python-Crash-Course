"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        odometer_reading = f"The {self.year} {self.make} {self.model} has {self.odometer_reading} miles on it."
        return odometer_reading

    def update_odometer(self, mileage):
        """
        Set odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery(make, model, year)

class Battery(Car):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, make, model, year, battery_size=75):
        """Initialize the battery's attributes"""
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        battery_size_statement = f"The {self.year} {self.make} {self.model} has a {self.battery_size}-kWh battery."
        return battery_size_statement

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        battery_range_statement = f"The {self.year} {self.make} {self.model} has a {self.battery_size}-kWh battery "
        battery_range_statement += f"and can go about {range} miles on full charge."
        return battery_range_statement

    def upgrade_battery(self):
        """Checks the battery size and sets the capacity to 100 if it isn't already."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the 75-kWh battery to 100-kWh.")
        else:
            print("The battery is already upgraded.")