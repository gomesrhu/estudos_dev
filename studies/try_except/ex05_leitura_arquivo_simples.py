
try:
    with open('dados.txt', 'r') as my_file:
        print(read(my_file))
except FileNotFoundError:
    print('File not found')
