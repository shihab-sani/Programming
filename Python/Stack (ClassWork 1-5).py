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
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.print_stack()
s.push_stack(1)
s.print_stack()