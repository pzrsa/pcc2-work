class Car:
    """
    A simple attempt of representing a car.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name.
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage.
        """
        print(
            f"The {self.model.title()} has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Update the car's mileage to a given value.
        Reject the change if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(
                f"You cannot roll back an odometer!\nThe {self.model.title()} still has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        """
        self.odometer_reading += miles


class Battery:
    """
    A simple attempt to model a battery for an electric car.
    """

    def __init__(self, battery_size=75):
        """
        Initialize the battery's attributes.
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """
        Prints a statement about the range the battery provides.
        """

        if self.battery_size == 75:
            range = 250
        elif self.battery_size == 100:
            range = 400

        print(f"This car can go about {range} miles on a full charge.")


    def upgrade_battery(self):
        if self.battery_size < 100:
            print(f"\nUpgrading the {self.battery_size}kWh battery to 100kWh")
            self.battery_size = 100
            print(f"\nUpgraded your car's battery to {self.battery_size}kWh!")
        elif self.battery_size >= 100:
            print("You car is all good, no need to upgrade for now.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """
        Electric cars don't have gas tanks.
        """
        print("This car does not require a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.upgrade_battery()