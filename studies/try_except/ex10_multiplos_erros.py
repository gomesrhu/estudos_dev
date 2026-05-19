try:
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))#string should be int

    if n1 < n2:
        sum_nums = n1 + n2

    print(sum_nums)#if n1 >= n2 will raise NameError
except ValueError:
    print('Invalid value')
except NameError:
    print('Varible not defined')
except Exception as e:
    print(f'Ordinary error. Description: {e}')

