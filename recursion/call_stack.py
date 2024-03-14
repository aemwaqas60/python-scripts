def func_three():
    print(f'Three')


def func_two():
    func_three()
    print(f'Two')


def func_one():
    func_two()
    print(f'One')


print(f'function calling  :')
func_one()
