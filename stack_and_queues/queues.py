class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def enqueue(self, value):  # TC O(1)
        newNode = Node(value)

        if self.length == 0:
            self.start = newNode
            self.end = newNode
        else:
            self.end.next = newNode
            self.end = newNode
        self.length += 1
        return True

    def dequeue(self):  # TC O(1)
        if self.length == 0:
            return None
        temp = self.start
        if self.length == 1:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next
        temp.next = None
        self.length -= 1
        return temp.value

    def print_queue(self):  # TC O(n)
        temp = self.start
        while temp:
            print(f"{temp.value}", end=' ')
            temp = temp.next


myQueue = Queue()
print(f'Enqueued 1 to 10 new elements : ')
for i in range(1, 11):
    myQueue.enqueue(i)

myQueue.print_queue()
print(f'\nDeque element: {myQueue.dequeue()}')
myQueue.print_queue()
print(f'\nDeque element: {myQueue.dequeue()}')
myQueue.print_queue()
print(f'\nDeque element: {myQueue.dequeue()}')
myQueue.print_queue()
