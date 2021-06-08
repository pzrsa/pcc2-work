"A class that represents different types of users."

from user import User


class Privileges:
    "Representation of privileges."

    def __init__(self, privileges):
        self.privileges = ['can add posts', 'can edit posts',
                           'can delete posts', 'can ban users']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\nAn Admin {privilege}.")


class Admin(User):
    "Representation of an Admin"

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(self)
