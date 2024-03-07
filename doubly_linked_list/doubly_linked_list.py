class Node:
    def __init__(self, value):
        self.value = value,
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):  # TC O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return True
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1
        return True

    def pop(self):  # TC O(1)
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return True

    def prepend(self, value):  # TC O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return True
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return True

    def pop_first(self):  # TC O(1)
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return True

    def get_value(self, index):  # TC O(n/2)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):  # TC O(n)
        if index < 0 or index >= self.length:
            return None
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def print_list(self):  # TC O(n)
        temp = self.head
        while temp:
            print(f'Node : {temp.value}')
            temp = temp.next


myList = DoublyLinkedList()
print(f"--- Appending new nodes values 10 to 15  ---")

for i in range(10, 20):
    myList.append(i)
myList.print_list()

print(f'pop node : {myList.pop()}')
print(f'pop node : {myList.pop()}')

myList.print_list()

print(f'prepend node 9: {myList.prepend(9)}')
myList.print_list()

print(f'pop node from start : {myList.pop_first()}')
myList.print_list()

print(f'get node value at 3: {myList.get_value(3).value}')
myList.print_list()

print(f'set node value 33 at 3 index : {myList.set_value(3, 33)}')
myList.print_list()
