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
    
    # Solution-05
    def push_stack(self,value):
        temp = Stack()
        while self.peek() > value:
            temp.push(self.peek())
            self.pop()
    
        self.push(value)
        
        while not temp.is_empty():
            self.push(temp.peek())
            temp.pop()
            
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.stack.print_linked_list()
            
class Queue:
    def __init__(self):
        self.queue = Singly_Linked_List()
        
    def size(self):
        return self.queue.size
    
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
        
# Solution-09
class My_Queue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        
    def enqueue(self,data):
        self.stack_2.push(data)
        while not self.stack_2.is_empty():
            self.stack_1.push(self.stack_2.peek())
            self.stack_2.pop()   
            
    def print_my_queue(self):
        self.stack_1.print_stack()
  
# Solution-01        
def reverse_string(str):
    stack = Stack()
    
    for word in str:
        stack.push(word)
    while not stack.is_empty():
        print(f"{stack.peek()} : {ord(stack.peek())}")
        stack.pop()    

# Solution-02 
def bracket_balance(brackets):
    s = Stack()
    
    for i in brackets:
        if i == "(" or i == "{" or i == "[":
            s.push(i)
        else:
            if s.is_empty():
                return False
            elif s.peek() == "(":
                if i != ")":
                    return False
            elif s.peek() == "{":
                if i != "}":
                    return False            
            elif s.peek() == "[":
                if i != "]":
                    return False
            s.pop()
                
    if s.is_empty():
        return True
    else:
        return False

# Solution-03
def keep_largest_on_top(stack):
    helping_stack = Stack()
    large = stack.peek()
    while not stack.is_empty():
        value = stack.peek()
        if large < value:
            large = value
        helping_stack.push(stack.peek())
        stack.pop()
    
    while not helping_stack.is_empty():
        value = helping_stack.peek()
        helping_stack.pop()
        if large != value:
            stack.push(value)
    stack.push(large)
    return stack

# Solution-04
def balance_two_stack(stack1,stack2):
    helping_stack1 = Stack()
    helping_stack2 = Stack()
    sum1 = 0
    sum2 = 0
    while not stack1.is_empty():
        sum1 += stack1.peek()
        helping_stack1.push(stack1.peek())
        stack1.pop()
    while not stack2.is_empty():
        sum2 += stack2.peek()
        helping_stack2.push(stack2.peek())
        stack2.pop()
    
    if sum1 > sum2:
        sum0 = sum1-sum2
        while not helping_stack2.is_empty():
            stack2.push(helping_stack2.peek())
            helping_stack2.pop()
        stack2.push(sum0)
        while not helping_stack1.is_empty():
            stack1.push(helping_stack1.peek())
            helping_stack1.pop()
    else:
        sum0 = sum2-sum1      
        while not helping_stack1.is_empty():
            stack1.push(helping_stack1.peek())
            helping_stack1.pop()
        stack1.push(sum0)  
        while not helping_stack2.is_empty():
            stack2.push(helping_stack2.peek())
            helping_stack2.pop() 

# Solution-06           
def reverse_add(k,queue):
    stack = Stack()
    for _ in range(k):
        stack.push(queue.peek())
        queue.dequeue()
    
    while not stack.is_empty():
        queue.enqueue(stack.peek())
        stack.pop()

# Solution-07        
def odd_even(queue):
    team_A = Queue()
    team_B = Queue()
    while not queue.is_empty():
        if queue.peek() % 2 == 0:
            team_A.enqueue(queue.peek())
            queue.dequeue()
        else:
            team_B.enqueue(queue.peek())
            queue.dequeue()
    team_A.print_queue()
    team_B.print_queue()
    
# Solution-08
def binary_decimal(value):
    queue = Queue()
    
    for i in range(value+1):
        queue.enqueue(str(bin(i)[2::]))
    queue.print_queue()


# s = Queue()
# s.enqueue(1)
# s.enqueue(2)
# s.enqueue(3)
# s.print_queue()
# s1 = My_Queue()
# s1.enqueue(1)
# s1.enqueue(2)
# s1.enqueue(3)
# s1.print_my_queue()
