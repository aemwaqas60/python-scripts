def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


# nested decorators
# nested decorator follows the bottom to top approach
@decor
@decor1
def num():
    return 10


# nested decorators
# nested decorator follows the bottom to top approach

@decor1
@decor
def num2():
    return 10


def strong(func):
    def wrapper(*args, **kwargs):
        return f"<strong >{func()} < / strong >"

    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func()} < / i>"

    return wrapper


# nested decorators
# nested decorator follows the bottom to top approach
@italic
@italic
@strong
def introduction():
    return "This is a basic program"


#
# print(f'Function calling using decorator : {num2()}')
# print(f'Function calling using decorator : {num()}')

print(introduction())
