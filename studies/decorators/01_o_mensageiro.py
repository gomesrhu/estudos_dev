from functools import wraps

def simple_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting function...")
        resultado = func(*args, **kwargs)
        print("Function finished")
        return resultado
    return wrapper


@simple_decorator
def greeter():
    print("Hello buddy!")
