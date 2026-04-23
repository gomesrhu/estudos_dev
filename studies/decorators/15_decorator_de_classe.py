from datetime import datetime
from functools import update_wrapper


class TimeRecord:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):

        result = self.func(*args, **kwargs)

        timestamp = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

        with open('function_log.txt', 'a') as my_file:
            my_file.write(f"Call function {self.func.__name__} at:{timestamp} \n")

        return result


@TimeRecord
def decorated_class_sum(x, y):
    return x+y

