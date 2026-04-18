from time import time
from functools import wraps

def limit(max_calls, secs_interval):
    def decorator(func):
        counter = 0
        time_limit = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter, time_limit
            now = time()

            #check if current time is bigger than time limit, if so reset counter and calculate new time limit
            if now > time_limit:
                counter = 0
                time_limit = now + secs_interval
                print(f"Reset calls counter and time limit...")

            #if there's still calls, then execute function
            if counter < max_calls:
                counter += 1
                print(f"Function: {func.__name__} Execution: {counter}/{max_calls}")
                return func(*args, **kwargs)
            #if function had been call more than "max calls times" raise RuntimeError
            else:
                raise RuntimeError(f"Function '{func.__name__}' ran more than {max_calls} in {secs_interval} seconds.")

        return wrapper
    return decorator


@limit(3, 2.5)#max_calls = 3, secs_interval=2.5 decorated function can only execute 3 times in 2.5 secs
def limited_sum(x, y):
    return x+y
