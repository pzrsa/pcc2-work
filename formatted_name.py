def formatted_name(first_name, last_name, middle_name=''):
    '''Returns the full name formatted'''
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(formatted_name('parsa', 'mesgarha'))