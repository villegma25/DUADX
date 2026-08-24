from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


def validate_user_age(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, User):
                if arg.age < 18:
                    raise ValueError("User must be at least 18 years old.")
        
        for arg in kwargs:
            if isinstance(arg, User):
                if arg.age < 18:
                    raise ValueError("User must be be at least 18 years old.")
                
        return func(*args, **kwargs)
    return wrapper


@validate_user_age
def access_adult_site(user):
    print("Access granted.")


# Test
u2young = User(date(2019, 3, 1))
uold = User(date(2000, 6, 5))

access_adult_site(uold)      #  Should print: Access granted.
access_adult_site(u2young)   #  Should raise: ValueError
