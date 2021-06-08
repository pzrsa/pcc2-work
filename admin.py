class User:
    "Representation of a User"
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


class Admin(User):
    "Representation of an Admin"

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add posts', 'can edit posts', 'can delete posts', 'can ban users']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\n{self.first_name.title()} {privilege}.")


parsa = Admin('parsa', 'mesgarha', 17)
parsa.show_privileges()