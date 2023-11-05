class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_after(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
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
        
class Queue:
    def __init__(self):
        self.queue = Singly_Linked_List()
    
    def enqueue(self,data):
        self.queue.add_after(data)
    
    def dequeue(self):
        self.queue.delete_before()
    
    def is_empty(self):
        if self.queue.size == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.queue.head.data
        
    def print_queue(self):
        self.queue.print_linked_list()
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print_queue()
print(q.peek())
q.dequeue()
q.dequeue()
q.print_queue()