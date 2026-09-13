"""реализация стека и основных методов"""

class ArrayStack:
    def __init__(self, initial_capacity = 5): # инициализируем нужные поля
        self._capacity = initial_capacity # начальная вместимость стека
        self._values = [None] * self._capacity
        self._index = 0 # индекс следующей свободной ячейки
        
    def push(self, value): # реализация стандартного метода append, ведь только ебучие казуалы будут юзать встроенные методы
        #self._values.append(value)
        if self._index == self._capacity:
            self._resize() # метод для увеличения размера стека, в случае его переполнения
        self._values[self._index] = value # записываем в первую свободную ячейку новое значение
        self._index += 1 # увеличиваем индекс, что бы он указывал на следующее свободное место
        
            
    def _resize(self): # вызывается если индекс пустого элемента = вместимости стека
        new_capacity = int(self._capacity * 1.5) + 1
        new_values = [None] * new_capacity
        
        for i in range(self._index):
            new_values[i] = self._values[i]
        
        self._values = new_values
        self._capacity = new_capacity
        
    def pop(self): # реализация стандартного метода pop, ведь только ебучие казуалы будут юзать встроенные методы 
        if self.is_empty():
            raise IndexError('stack_is_empty')
        self._index -= 1 # сначала уменьшаем индекс, а потом ссылаемся на элемент, потому что нам надо удалить элемент, а индекс всегда = индексу последнего элемента + 1
        value = self._values[self._index]
        self._values[self._index] = None  # перезаписываем значение на None, что бы условные ссылки на большие объекты не валялись тут,
                                            #может работать и без этого, элемент потом все равно перезапишется через push
        return value
    
    def peek(self): # возвращает последнее значение в стеке
        if not self.is_empty():
            return self._values[self._index - 1] # индекс всегда = индексу последнего элемента + 1
        raise IndexError('stack_is_empty')
    
    def is_empty(self): # возвращает True если в стеке нет элементов
        return self._index == 0 
    


# использование:

stack = ArrayStack()

stack.push(20)
stack.push(30)
stack.push(40)

# стек : 20 -> 30 -> 40 -> остальное место занято None

stack.pop()

# стек : 20 -> 30 -> остальное место занято None

print(stack.peek()) #30