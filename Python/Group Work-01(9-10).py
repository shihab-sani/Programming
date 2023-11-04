class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List:
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
            new_node.prev = current
    
    def add_node_after_value(self,given_value,new_value):
        if self.head == None:
            print("The list is empty")
        else:
            current = self.head
            while current != None:
                if current.data != given_value:
                    current = current.next
                else:
                    break
            if current == None:
                print("Given value not found in the list")
            else:
                new_node = Node(new_value)
                new_node.next = current.next
                new_node.prev = current
                if current.next != None:
                    current.next.prev = new_node
                current.next = new_node
    
    def insert_sorted(self,value):
        new_node = Node(value)
        if self.head == None:
            print("The list is empty")
        else:
            current = self.head
            while current != None:
                if current.data > value:    
                    new_node.next = current
                    new_node.prev = current.prev
                    if current.prev != None:
                        current.prev.next = new_node
                    else:
                        self.head = new_node
                    current.prev = new_node
                    break
                elif current.next == None:
                    current.next = new_node
                    new_node.prev = current
                    break
                current = current.next            
                                
    def print_node(self):
        if self.head == None:
            print("The list is empty")
        else:
            current =self.head
            while current != None:
                print(current.data, end="<->")
                current = current.next
            print() 
            
d = Doubly_Linked_List()
d.add_node(3)
d.add_node(5)
d.add_node(8)
d.add_node(10)
d.add_node(12)
d.print_node()
d.add_node_after_value(3,4)
d.print_node()
d.insert_sorted(13)
d.print_node()

