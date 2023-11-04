class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        
    def add_node(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def add_first(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def add_specifically(self,value,data):
        if self.head == None:
            print("List is empty")
        else:
            current = self.head
            while current != None:
                if current.data != value:
                    current = current.next
                else:
                    break
            if current == None:
                print("Given value not found in the list")
            else:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
    
    def remove_first(self):
        if self.head == None:
            print("List is empty")
        else:
            x = self.head
            self.head = self.head.next
            x = None
    
    def remove_specifically(self,data):
        if self.head == None:
            print("List is empty")
        elif self.head.data == data:
            x = self.head
            self.head = self.head.next
            x = None            
        else:
            current = self.head
            while current != None:
                if current.next.data != data:
                    current = current.next
                else:
                    break
            x = current.next
            current.next = current.next.next
            x = None
    
    def remove_last(self):
        if self.head == None:
            print("List is empty")
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            x = current.next
            current.next = None
            x = None
                              
    def print_linked_list(self):
        current = self.head
        while current != None:
            print(current.data,end="->")
            current = current.next 
        print()
            

s = Singly_Linked_List()
s.add_node(5)
s.add_node(6)
s.add_node(7)
s.add_node(8)
s.print_linked_list()
s.add_first(5)
s.print_linked_list()
s.add_specifically(20,30)
s.print_linked_list()
#s.remove_first()
#s.print_linked_list()
#s.remove_specifically(10)
#s.remove_last()
#s.print_linked_list()