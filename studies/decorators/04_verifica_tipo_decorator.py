from functools import wraps

def check_type(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        if not all(isinstance(arg, int) for arg in all_args):
            print("Some argument isn't of the 'int' type...")
            return None
        print("Everything is fine...")
        return func(*args, **kwargs)
    return wrapper

@check_type
def my_numbers(*pos_numbers, **kwargs_numbers):
    return pos_numbers, kwargs_numbers

print(my_numbers(3, 1, 4, x=10))#
