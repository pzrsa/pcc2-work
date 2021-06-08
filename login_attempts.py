class User:

    def __init__(self, first_name, last_name, age, login_attempts):
        """
        Initialize attributes for the user
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\nThe users first name is {self.first_name.title()}.")
        print(f"The users last name is {self.last_name.title()}.")
        print(f"The user is {self.age} years old.")

    def greet_user(self):
        print(f"Hello there, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name.title()}'s login attempts have now been increased to {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"{self.first_name.title()}'s login attempts have now been reset to {self.login_attempts}") 



parsa = User('parsa', 'mesgarha', 17, 2)

for _ in range(5):
    parsa.increment_login_attempts()

parsa.reset_login_attempts()