n1 = input('enter number 1: ')
n2 = input('enter number 2: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    sum_ints = n1 + n2
except (ValueError, TypeError):
    print('error converting numbers to int or sum')
else:
    print(f'{n1} + {n2} = {sum_ints}')
