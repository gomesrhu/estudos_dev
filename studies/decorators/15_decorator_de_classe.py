from time import time
from datetime import datetime

class TimeRecord:
    def __init__(self):
        self.time = ""

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            timestamp = datetime.now()
            formatted_timestamp = timestamp.strftime("%d/%m/%Y - %H:%M:%S")
            self.time = formatted_timestamp

            with open('function_log.txt', 'a') as my_file:
                my_file.write(f"{self.time} \n")

            return result
        return wrapper

class_decorator = TimeRecord()

@class_decorator
def decorated_class_sum(x, y):
    return x+y
