class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurants name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!")



class IceCreamStand(Restaurant):
    """
    A simple representation of an ice cream stand at a restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'pistachio', 'strawberry', 'bubblegum']

    def describe_flavors(self):
        for flavor in self.flavors:
            print(f"\nWe have a {flavor} flavor ice cream")
    

my_ice_cream = IceCreamStand('gokyuzu', 'turkish')
my_ice_cream.describe_flavors()