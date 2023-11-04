class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_before(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def delete_before(self):
        if self.head == None:
            return False
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
            
    def print_linked_list(self):
        current = self.head
        while current != None:
            print(current.data,end="->")
            current = current.next 
        print()
        
class Stack:
    def __init__(self):
        self.stack = Singly_Linked_List()
    
    def size(self):
        return self.stack.size
    
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def push(self,data):
        self.stack.add_before(data)
    
    def pop(self):
        self.stack.delete_before()
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack.head.data
    
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.stack.print_linked_list()
            
s = Stack()
s.push(0)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()
print(s.size())
print(s.pop())
print(s.size())