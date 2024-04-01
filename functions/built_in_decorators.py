from abc import abstractmethod


# class method decorator
class Bank:
    interestRate = 2.2

    @classmethod
    def getInterestRate(cls):
        return cls.interestRate


print(f'Interest Rate : {Bank.getInterestRate()}')


class Shape:
    @abstractmethod
    def area(self):
        pass


# abstract decorator
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


square = Square(20)

print(f'\nArea of square is : {square.area()}')


# Static methods are simply utility methods that are not bound to a class or an instance of the class
class Person:

    def __init__(self):
        self._name = 0

    @staticmethod
    def greetings():
        print(f"\nHi, welcome in python 3 using static method ")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


Person.greetings()
# setting name using setter
p = Person()
p.name = "Abdus slam"

# getting name using getter
print(f'Person name {p.name}')
