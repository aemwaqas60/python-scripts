# global and local scope using function

a = 1


def f():
    print(f'Inside f() : {a}')


def g():
    a = 2
    print(f'Inside g() : {a}')


def h():
    global a
    a = 3
    print(f'Inside h() : {a}')


# Global scope

print(f'Global a : {a}')
f()
print(f'Global a : {a}')
g()
print(f'Global a : {a}')
h()
print(f'Global a : {a}')
