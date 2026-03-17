def my_decorator(original_function):
    def wrapper(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = original_function(*args, **kwargs)
        print("Return value:", result)
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

# Test the decorated function
add(3, 4)
