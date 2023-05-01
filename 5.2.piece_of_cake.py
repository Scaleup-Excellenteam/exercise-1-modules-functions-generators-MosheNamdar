def get_recipe_price(dictionary, **kwargs):
    price = 0
    optional = get_optional_values(**kwargs)

    for key, value in kwargs.items():
        for key_of_dict in dictionary:
            if key == key_of_dict and key not in optional:
                price += ((dictionary[key_of_dict] * value) / 100)

    return price


def get_optional_values(**kwargs):
    optional = []
    for key, value in kwargs.items():
        if key == "optional":
            optional = value

    return optional

#print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
#print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
#print(get_recipe_price({}))
