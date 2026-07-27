#Python script

# We require brand and model but allow any number of extra specs

def make_smartphone(brand, model, **phone_specs):
    """Build a dictionary containing everything we know about a phone"""

    #Add the required parameters to the dictionary that **kwardgs created
    phone_specs['brand_name'] = brand
    phone_specs['model_name'] = model

    # Hand the complete dictionary back to the program

    return phone_specs

# We pass the two required arguments , plus three arbitrary keyword arguments

my_phone = make_smartphone('Apple', 'iPhone 16',
                           storage='256GB',
                           color='Midnight',
                           has_5g=True)

print(my_phone)


