class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"\nThe users first name is {self.first_name}.")
        print(f"The users last name is {self.last_name}.")
        print(f"The user is {self.age} years old.")

    def greet_user(self):
        print(f"Hello there, {self.first_name} {self.last_name}")


parsa = User('Parsa', 'Mesgarha', 17)

parsa.describe_user()
parsa.greet_user()

steve = User('Steve', 'Jobs', 66)
steve.describe_user()
steve.greet_user()
