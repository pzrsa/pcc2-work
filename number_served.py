class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"\nThe restaurants name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!")


    def set_number_served(self, customers):
        self.number_served = customers
        return self.number_served

    def increment_number_served(self, customers):
        self.number_served += customers
        return self.number_served

        
restaurant = Restaurant('Gokyuzu', 'Turkish', 2)

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)

print(f"The restaurant has served {restaurant.number_served} customers.")

restaurant.increment_number_served(30)

print(f"The restaurant has now served {restaurant.number_served} throught out the day.")