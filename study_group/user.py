"""A set of classes used to represent account users and their privileges."""

class User:
    """An attempt to model the attributes of a user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Describe user attributes."""
        user_description = f"User: {self.first_name} {self.last_name}"
        user_description += f"\n Username: {self.username}"
        user_description += f"\n Email: {self.email}"
        user_description += f"\n Location: {self.location}"
        return user_description
    
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        user_greeting = f"Welcome, {self.first_name} {self.last_name}"
        return user_greeting

    def build_profile(self, first, last, **user_info):
        """Build a dictionary containing everything we know about a user."""
        user_info['first_name'] = first
        user_info['last_name'] = last
        return user_info
    
    def increment_login_attempts(self):
        """Increment the number of user login attempts."""
        self.login_attempts += 1
        logon_attempts_statement = f"{self.first_name} {self.last_name} has made {self.login_attempts} login attempt(s)."
        return logon_attempts_statement

    def reset_login_attempts(self):
        """Reset a user's total login attempts to 0."""
        self.login_attempts = 0
        reset_logon_attempts_statement = f"{self.first_name} {self.last_name}'s total login attempts are now {self.login_attempts}."
        return reset_logon_attempts_statement

class Admin(User):
    """Attempt to model the attributes of an Admin-level user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the attributes of an Admin-level user."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges(first_name, last_name, username, email, location)

class Privileges(User):
    """A class that stores an admin's privileges."""

    def __init__(self, first_name, last_name, username, email, location, privileges=[]):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = privileges

    def show_privileges(self):
        """Prints a statement that shows a list of privileges of an Admin-level user."""
        privilege_statement = f"\n{self.first_name} {self.last_name} has the current privileges of:"
        print(privilege_statement)
        for privilege in self.privileges:
            print(f"- {privilege}")