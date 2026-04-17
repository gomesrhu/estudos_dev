import time

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Waiting {seconds} seconds to execute function: '{func.__name__}'")
            time.sleep(seconds)
            resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@delay(1.5)#seconds=1.5 in this exemple
def no_recursion_factorial(n):
    if n > 1:
        total = 1
        for i in range(2, n+1):
            atual = total * i
            total = atual
    return total

