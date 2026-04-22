from functools import wraps

def upper_converter(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        formatted = str(func(*args, **kwargs)).upper()
        return formatted
    return wrapper

@upper_converter
def my_msg(msg):
    return msg

