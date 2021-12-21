from car import Car, ElectricCar

# Using an alias for importing modules
from car import ElectricCar as EC

# You can also import an entire module and then
# access the classes you need using dot notation.
import car

# Importing all classes from a module
# NOT RECOMMENDED - If you need to import 
# many classes from a module, you’re better off
# importing the entire module and using the 
# module_name.ClassName syntax.
from car import *

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_beetle.read_odometer()
my_beetle.increment_odometer(250)
my_beetle.read_odometer()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())