class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None
    
    def add_node(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        
    def get_average(self):
        if self.head == None:
            print("The list is empty")
        else:
            count = 0
            total = 0
            current = self.head
            while current != None:
                count += 1
                total += current.data
                current = current.next
            print(total/count)
            
    def num_of_occurrences(self,value):
        if self.head == None:
            print("The List is empty")
        else:
            count = 0
            current = self.head
            while current != None:
                if current.data == value:
                    count += 1
                current = current.next
            if count > 0:        
                print(count)
            else:
                print("The given value not found in the lsit")
    
    def find_max(self):
        if self.head == None:
            print("The List is empty")
        else:
            current = self.head
            maximum = current.data
            while current != None:
                if maximum < current.data:
                    maximum = current.data
                current = current.next
            print(maximum)
    
    def find_min(self):
        if self.head == None:
            print("The List is empty")
        else:
            current = self.head
            minimum = current.data
            while current != None:
                if minimum > current.data:
                    minimum = current.data
                current = current.next
            print(minimum)
                
    def data(self):
        if self.head == None:
            print("The List is empty")
        else:
            l = []
            current = self.head
            while current != None:
                l.append(current.data)
                current = current.next
            return l  
    
    def add_node_before_value(self,given_value,new_value):
        if self.head == None:
            print("The List is empty")
        else:
            if self.head.data == given_value:
                new_node = Node(new_value)
                new_node.next = self.head
                self.head = new_node
            else:  
                current = self.head  
                while current != None:
                    if current.next.data != given_value:                       
                        current = current.next
                    else:
                        break
                if current == None:
                    print("The given value not found")
                else:
                    new_node = Node(new_value)
                    new_node.next = current.next
                    current.next = new_node
        
    def delete_node(self,data):
        if self.head == None:
            print("The List is empty")
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
            
    def delete_even(self):
        if self.head == None:
            print("The List is empty")                      
        else:
            current = self.head
            while current != None:
                if (current.data % 2) == 0:
                    self.delete_node(current.data)
                current = current.next     
    
    def sorted_insert(self,value):
        if self.head == None:
            print("The List is empty")  
        else:
            current = self.head
            while current != None:
                if value < current.data:
                    self.add_node_before_value(current.data,value)
                    break
                elif current.next == None:
                    new_node = Node(value)
                    current.next = new_node
                    break
                current = current.next  
    
    def reverse_list(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
                        
    def print_node(self):
        if self.head == None:
            print("The List is empty")
        else:
            current = self.head
            while current != None:
                print(current.data,end="->")
                current = current.next 
            print()        
                
def compare_two_list(list_1,list_2):
    if list_1.data() == list_2.data():
        return True
    else:
        return False
        
        
s = Singly_Linked_List()
t = Singly_Linked_List()
s.add_node(5)
s.add_node(6)
s.add_node(7)
s.add_node(8)
s.get_average()
s.num_of_occurrences(7)
s.find_max()
s.find_min()
t.add_node(5)
t.add_node(6)
t.add_node(7)
t.add_node(7)
print(compare_two_list(s,t))
s.add_node_before_value(5,4)
s.print_node()
s.delete_even()
s.print_node()
s.sorted_insert(8)
s.print_node()
s.reverse_list()
s.print_node()






            