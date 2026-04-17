def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(n):
                try:
                    result = func(*args, **kwargs)
                    return result
                except:
                    count += 1
                    print(f"Attemp number: {count} to run the function: '{func.__name__}' ")
            print(f"All {n} attempts failed")
        return wrapper
    return decorator

@retry(3)
def dangerous_division(x, y):
    return x/y


