def interval(min, max):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not (min < result < max):
                error_msg = f"Error.Result ({result}) of the decorated function '{func.__name__}' isn't between {min} and {max}"
                raise RuntimeError(error_msg)
            return result
        return wrapper
    return decorator

@interval(2, 10)
def decorated_sum(a, b):
    return a+b
