class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.dataMap = [None] * size

    def __hash(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 23) % len(self.dataMap)
        return myHash

    def set_value(self, key, value):  # TC O(1)
        index = self.__hash(key)
        if self.dataMap[index] is None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])
        return True

    def print_hash(self):
        for listItem in self.dataMap:
            if listItem is not None:
                for j in listItem:
                    print(f'{j}', end=' ')
            print(f"\n")

    def get_value(self, key):  # TC O(1) in ideal case, O(n) in worst case
        index = self.__hash(key)
        if self.dataMap[index] is None:
            return False
        for i in range(len(self.dataMap[index])):
            if self.dataMap[index][i][0] == key:
                return self.dataMap[index][i][1]
        return False


myHashTable = HashTable()

print(f"\nInsert values in hash table using (key, value ) : ")
myHashTable.set_value('age', 31)
myHashTable.set_value('apartment', 21)
myHashTable.set_value('houseNo', 301)

print(f"\nHash table  : ")
myHashTable.print_hash()

print(f'Find value using key \'age\' {myHashTable.get_value("age")}')
print(f'Find value using key \'apartment\' {myHashTable.get_value("apartment")}')
print(f'Find value using key \'houseNo\' {myHashTable.get_value("houseNo")}')
