class Deque:
    def __init__(self):
        self.__deque=["elemen",12,3,4]

    def __str__(self):
        return f'{self.__deque}'

    def add_first(self, item):
        self.__deque.insert(0, item)

    def add_last(self, item):
        self.__deque.append(item)

    def vacio(self):
        return len(self.__deque) == 0

    def remove_first(self):
        return None if self.vacio() else self.__deque.pop(0)

    def remove_last(self):
        return None if self.vacio() else self.__deque.pop()


test = Deque()

print(test)

test.add_first(1); test.add_last(9) 

print(test)

test.remove_first(); test.remove_last()

print(test)
