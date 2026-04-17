def cache(func):
    args_dict = {}
    def wrapper(*args, **kwargs):
        if args in args_dict: #if the arguments already are in the dict, then just return the respective value
            return args_dict[args]
        else:# include the arguments as keys to the dict and result as it's value
            result = func(*args, **kwargs)
            args_dict[args] = result
            return result
    return wrapper

@cache
def cache_sum(x, y):
    return x+y
    
