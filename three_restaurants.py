class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n\nThe restaurants name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!")


restaurant = Restaurant('Gokyuzu', 'Turkish')
second_restaurant = Restaurant('Wagamama', 'Japanese')
third_restaurant = Restaurant('Beer and Burger', 'American')


restaurant.describe_restaurant()
restaurant.open_restaurant()


second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()

third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()
