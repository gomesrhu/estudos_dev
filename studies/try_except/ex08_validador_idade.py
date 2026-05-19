try:
    age = int(input('Enter age: '))

    invalid_age = 0 > age or age > 150
    if invalid_age:
        raise Exception
except Exception:
    raise ValueError('Invalid age')
else:
    print(f'Age registration successful')
