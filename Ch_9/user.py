class User:
    """Class to collect details about users."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        """Describe details about a user."""
        print(f"User: \nFirst name: {self.first_name}\nLast name: {self.last_name}")
    
    def greet_user(self):
        """Greets a provided user."""
        print(f"Welcome, {self.first_name} {self.last_name}!")
    
    def build_profile(self, first, last, **user_info):
        """Build a dictionary containing everything we know about a user."""
        user_info['first_name'] = first
        user_info['last_name'] = last
        return user_info

class Admin(User):
    """Define the parameters of the Admin class of user."""

    def __init__(self, privileges):
        """Initialize the Admin user class"""
        self.privileges = privileges


# class Privileges:






user_profile = User.build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')