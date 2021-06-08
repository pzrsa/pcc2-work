# cars = ['mercedes', 'audi', 'porsche', 'bmw']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# cars.sort()
# print(cars)
# # Sort in reverse alphabetical order
# cars.sort(reverse=True)
# print(cars)
# # Sorted function temporarily sorts the list instead
# cars = ['lexus', 'audi', 'porsche', 'bmw']
# print("\nHere is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)
# # Reverse function sorts the list backwards but not alphabetically
# cars.reverse()
# print("\nHere is the reversed list:")
# print(cars)
# cars.reverse()
# print("\nHere is the list back to normal:")
# print(cars)
# # Len function finds the length of the list items
# length_cars = len(cars)
# print(length_cars)


def build_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = build_car('Audi', 'R8', color= 'Black', price='£100,000')

print(car)