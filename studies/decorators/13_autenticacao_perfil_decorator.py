def requires_profile(profile):
    def decorator(func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0].get("profile", None) == profile:
                print("Access allowed")
                return func(*args, **kwargs)
            else:
                error_msg = f"Error. User {args[0].get("name", None)} not allowed"
                raise PermissionError(error_msg)
        return wrapper
    return decorator


user1 = {
    "name":"John",
    "profile":"admin"
    }

user2 = {
    "name":"Liz",
    "profile":"user"
    }

@requires_profile("admin")
def delete_data(logged_user, data):
    """
    Delete system sensible data;

    Argument 'logged_user' MUST be the first positional argument.
    """
    return f"{logged_user.get("name", None)} deleted data: {data}"

