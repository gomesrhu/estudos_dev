def average(*args):
    try:
        mean = sum(args)/len(args)
    except Exception as e:
        print(f'Error: {e}')
    else:
        return mean
    finally:
        print('End processing')


