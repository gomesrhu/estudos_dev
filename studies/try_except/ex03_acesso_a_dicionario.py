my_dict = {
    'apple':4.98,
    'pearl':3.59,
    'blueberry':13.75,
    'strawberry':9.80,
    'banana':2.99
    }

get_fruit = str(input('Type a fruit name:   ')).lower()

try:
    my_dict[get_fruit]
except KeyError:
    print('The requested fruit isn\'t on the dictionary')
else:
    print(my_dict[get_fruit])
