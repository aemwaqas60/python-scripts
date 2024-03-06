class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(f"Node : {temp.value}")
            temp = temp.next

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return True
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            current = self.head
            while True:
                previous = current
                current = current.next
                if current.next is None:
                    break

            self.tail = previous
            previous.next = None
            self.length -= 1
            return current.value

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return True
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, value, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()

        temp = self.get(index - 1)
        removeNode = temp.next
        temp.next = removeNode.next
        removeNode.next = None
        self.length -= 1
        return True


myList = LinkedList()

for i in range(5):
    print(f'Append : {myList.append(i)}')  # Time complexity = O(1)
#
# for i in range(myList.length):
#     print(f'Pop : {myList.pop()}')  # Time complexity = O(n)


for i in range(6, 10):
    print(f'Prepend : {myList.prepend(i)}')  # Time complexity = O(1)

print(f'pop first node : {myList.pop_first()}')  # Time complexity = O(1)
print(f'pop first node : {myList.pop_first()}')  # Time complexity = O(1)
print(f'get node at 4th index : {myList.get(3)}')  # Time complexity = O(1)
print(f'Insert new node value 13 at 5th index : {myList.insert(13, 4)}')  # Time complexity = O(n)
print(f'Insert new node value 23 at 8th index : {myList.insert(23, 7)}')  # Time complexity = O(n)

print(f'----- Before remove list :  -----')
myList.print_list()

print(f'Remove node from start : {myList.remove(0)}')  # Time complexity = O(1)
print(f'Remove Node node at 7th index : {myList.remove(6)}')  # Time complexity = O(n)

print(f'----- After remove list :  -----')

myList.print_list()
