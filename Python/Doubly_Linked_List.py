class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self) :
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
            
    def add_before(self,value,new_value):
        if self.head == None:
            print("The list is empty")
        else:
            if self.head.data == value:
                new_node = Node(new_value)
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                current = self.head
                while current != None:
                    if current.data == value:
                        new_node = Node(new_value)
                        new_node.next = current
                        new_node.prev = current.prev
                        current.prev.next = new_node
                        current.prev = new_node
                        break
                    current = current.next
                if current == None:
                    print("The given value not found in the list")
                    
    def add_after(self,value,new_value):
        if self.head == None:
            print("The list is empty")
        else:
            current = self.head
            while current != None:
                if current.data == value:
                    new_node = Node(new_value)
                    new_node.next = current.next
                    new_node.prev = current
                    if current.next != None:
                        current.next.prev = new_node
                    current.next = new_node
                    break
                current = current.next
            if current == None:
                print("The given value not found in the list")
        
    def sorted_insert(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.data > data:
                    new_node = Node(data)
                    self.add_before(current.data,new_node.data)
                    break
                current = current.next      
            if current.next == None:
                new_node = Node(data)
                self.add_after(current.data,new_node.data)
    
    def reverse_list(self):
        if self.head == None:
            print("The list is empty")
        else:
            temp = None
            current = self.head
            while current != None:
                temp = current.prev
                current.prev = current.next
                current.next = temp
                current = current.prev
            if temp != None:
                self.head = temp.prev
                
    def delete_node(self,data):
        if self.head == None:
            print("The list is empty")
        else:
            if self.head.data == data:
                temp = self.head
                self.head = self.head.next
                temp = None
            else: 
                current = self.head
                while current != None:
                    if current.data == data:
                        temp = current
                        current.prev.next = current.next
                        if current.next != None:
                            current.next = current.prev
                        temp = None
                        break
                    current = current.next
                if current == None:
                    print("The given data not in the list")
                
    def print_node(self):
        current = self.head
        while current != None:
            print(current.data,end="<->")
            current = current.next
        print()
        
l = Doubly_Linked_List()
l.add_node(5)
l.add_node(6)
l.add_node(7)
l.add_node(8)
l.print_node()
l.add_before(5,4)
l.print_node()
l.add_after(8,9)
l.print_node()
l.sorted_insert(3)
l.print_node()
l.delete_node(10)
l.print_node()
l.reverse_list()
l.print_node()


