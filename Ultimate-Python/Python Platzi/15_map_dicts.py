items = [
    {
        'product': 'Camisa',
        'price': 100
    },
    {
      'product': 'Pantalones',
        'price': 300
    },
{
      'product': 'Shorts',
        'price': 250
    },
]
prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)