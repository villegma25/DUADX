def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be numbers")
        
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError("All arguments must be numbers")
        
        return func(*args, **kwargs)  # Call the original function
    return wrapper  # Return the inner function


@validate_numbers
def multiply(x,y):
    return x * y

print(multiply(3, 5))
print(multiply(3, "five"))