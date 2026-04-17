def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_string = func(*args, **kwargs)
            formated_string = f"{text} {func_string}"
            return formated_string
        return wrapper
    return decorator

@prefix("Here's the prefix")
def saudacao(msg):
    return msg

print(saudacao("and this is what will be 'prefixed'"))
