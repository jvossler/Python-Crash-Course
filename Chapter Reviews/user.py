"""A set of classes used to represent account users and their privileges."""

class User:
    """A simple attempt to model a user."""
    
    def __init__(self, first_name, last_name):
        """Initialize first_name and last_name attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0
        
    def describe_user(self):
        """
        Describe the user.
        Return a full name, neatly formatted.
        """
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nThe user's name is {full_name}.")
            
    def greet_user(self):
        """Simulate greeting the user."""
        print(f"\nWelcome, {self.first_name}!")
    
    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0
        
    def show_login_attempts(self):
        """Print the value of login_attempts."""
        print(f"\nThe user {self.first_name} {self.last_name} has attempted to "
              f"login {self.login_attempts} times.")
        
        
# class Admin(User):
#     """A simple attempt to model an admin user."""
    
#     def __init__(self, first_name, last_name):
#         """Initialize first_name and last_name attributes."""
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()
        
#     def show_privileges(self):
#         """Print the privileges of the admin user."""
#         self.privileges.show_privileges()
    
#     def show_admin_privileges(self):
#         """Print the privileges of the admin user."""
#         self.privileges.show_privileges()