#базовая реализация связаного списка без указателя end

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Linked_list:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = ' -> ' if current_node.next else '\n')
            current_node = current_node.next
            

    def remove(self):
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
            
        current_node.next = None
                
            
        
        
linked_list1 = Linked_list()
linked_list1.append(50)
linked_list1.append([2,3,4])
linked_list1.append('hello')
linked_list1.remove()

linked_list1.print_list()