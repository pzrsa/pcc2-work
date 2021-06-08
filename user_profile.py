def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('steve', 'jobs', location = 'palo alto', field = 'technology')


user_profile = build_profile('parsa', 'mesgarha', location = 'London', age = 17, gender = 'male')

print(user_profile)