# parsa = {
#     'first_name': 'parsa',
#     'last_name': 'mesgarha',
#     'age': 17,
#     'city': 'london',
# }
# print(parsa['first_name')
# print(parsa['last_name'])
# print(parsa['age'])
# print(parsa['city'])


def build_person(first_name, last_name, age=None):
    '''Returns a dictionary of information about a person'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

person = build_person('parsa', 'mesgarha', age=17)
print(person)
