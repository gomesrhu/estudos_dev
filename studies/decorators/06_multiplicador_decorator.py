from functools import wraps

def generic_multiplicator(valor):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            retorno_func = func(*args, **kwargs)
            resultado = retorno_func * valor
            return resultado
        return wrapper
    return decorator


@generic_multiplicator(3)
def decorated_sum(a, b):
    return a+b

