from functools import wraps

def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("sentence inside wrapper")
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def minha_mensagem(msg):
    """This is my docstring and it's 'preserved' thanks to the functools.wraps"""
    print(msg)

# minha_mensagem("ordinary print")
# print(minha_mensagem.__name__)
# print(minha_mensagem.__doc__)
