"""реализация очереди и основных методов"""

class ArrayQueue:
    def __init__(self, capacity = 5):
        self.__values = [None] * capacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0
        
        
    def is_full(self):
        return len(self.__values) == self.__size
    
    
    def enqueue(self, value):
        if self.is_full():
            raise ValueError('queue is full')
        
        self.__values[self.__tail] = value
        self.__tail = (self.__tail + 1) % len(self.__values)
        self.__size += 1
    
    
    def is_empty(self):
        return self.__size == 0
    
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('queue is empty')
        value = self.__values[self.__head]
        self.__head = (self.__head + 1) % len(self.__values)
        self.__size -= 1
        
        return value 
    
    def peek(self):
        if self.is_empty():
            raise ValueError('queue is empty')
        return self.__values[self.__head]
    