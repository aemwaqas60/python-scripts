class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# stack work in LIFO (last in first out) order
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    # TC O(1) on top of the stack
    def push(self, value):
        newNode = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1

    # TC O(1) on top of the stack
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp.value

    def print_stack(self):  # TC O(n)
        temp = self.top
        while temp is not None:
            print(f'{temp.value}', end=" ")
            temp = temp.next


myStack = Stack()

print(f'Pushing 1 to 10 elements in stack : ')
for i in range(1, 3):
    myStack.push(i)
myStack.print_stack()

print(f'\nPop element : {myStack.pop()}')
myStack.print_stack()
print(f'\nPop element : {myStack.pop()}')
myStack.print_stack()
print(f'\nPop element : {myStack.pop()}')
myStack.print_stack()
