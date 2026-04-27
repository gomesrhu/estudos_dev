fruits = [
    'apple',
    'banana',
    'grape'
    ]

try:
    num = int(input('Enter a number:    '))
    print(f'{fruits[num]}')
except IndexError:
    print('Number out of index range')
except ValueError:
    print('Invalid number')


