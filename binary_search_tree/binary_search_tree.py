class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):  # TC : Ideal case O(log n), worst case O(n)
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True
        temp = self.root
        while True:
            if temp.value == newNode.value:
                return False
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right

    def display(self, value):  # TC : Ideal case O(log n), worst case O(n)
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return temp.value

        return False


myTree = BinarySearchTree()
print(f'\ninsert value : 2 {myTree.insert(2)}')
print(f'insert value : 3 {myTree.insert(3)}')
print(f'insert value : 1 {myTree.insert(1)}')

print(f'\nTree root : {myTree.root.value}')
print(f'Tree left node : {myTree.root.left.value}')
print(f'Tree right node : {myTree.root.right.value}')

print(f'\nFind value 2 : {myTree.display(2)}')
print(f'Find value 5 : {myTree.display(5)}')
