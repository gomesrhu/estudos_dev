def interval(min, max):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not (min < result < max):
                return f"Error. The result ({result}) of the decorated function '{func.__name__}' isn't between {min} and {max}"
            else:
                return result
        return wrapper
    return decorator

@interval(2, 10)#min=2 max=10 in this exemple
def decorated_sum(a, b):
    return a+b
