from car import Car

my_new_car = Car('audi', 'r8', 2021)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(100)

my_new_car.read_odometer()