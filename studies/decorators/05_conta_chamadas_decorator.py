from functools import wraps

def counts_calls(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        try:
            result = func(*args, **kwargs)
            count += 1
        except Exception as e:
            print(f"Error: {e}")
            return None
        print(f"Function '{func.__name__}' already run {count} times.")
        return result
    return wrapper

@counts_calls
def decorated_sum(x, y):
    return x+y



