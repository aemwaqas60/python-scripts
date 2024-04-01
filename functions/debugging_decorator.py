import functools


def make_if_happy(func):
    @functools.wraps(func)
    def wrapper():
        neutralMessage = func()
        happyMessage = neutralMessage + ", You are happy!"
        return happyMessage

    return wrapper


@make_if_happy
def speak():
    return "Hi"


print(speak())
print(speak.__doc__)
print(speak.__name__)
