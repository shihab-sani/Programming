class Sll_Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        
    def add_node(self,data):
        new_node = Sll_Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def print_linked_list(self):
        current = self.head
        while current != None:
            print(current.data,end="->")
            current = current.next 
        print()
        
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
            
    def print_node(self):
        current = self.head
        while current != None:
            print(current.data,end="<->")
            current = current.next
        print()

# 1. Write a recursive program to find the sum of first n numbers:

def sum_of_n(n):
    if n == 1:
        return 1
    return n + sum_of_n(n-1) 

# 2. Given a string, check whether the string is a palindrome or not.
# Write the recursive function. The function will return true or false:

def is_palindrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

# 3. Given an integer number, check whether it is palindrome or not. Write recursive function. It will return true or false:

def reverse_num(num):
    if num < 10:
        return num
    return int(str(num%10)+str(reverse_num(num//10)))

def palindrome_check(num):
    if num == reverse_num(num):
        return True
    return False

# 4. Given two integers, find and print the GCD (Greatest Common Divisor) of them. The function will return the GCD:

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd1(num1: int, num2: int) -> int:
    if num1 == 0 or num2 == 0:
        return 0
    gcd_value = min(num1, num2)
    if num1 % gcd_value == 0 and num2 % gcd_value == 0:
        return gcd_value
    return gcd1(max(num1, num2) - min(num1, num2), min(num1, num2))

# 5. Reverse a string using Recursion:

def reverse_str(string):
    if len(string) == 1:
        return string
    string_1 = reverse_str(string[1:]) + string[0]
    return string_1

# 6. Change the print_all function of a linked list to print all the value of nodes recursively:

def print_recursively(head):
    if head == None:
        return
    print(head.data,end="->")
    print_recursively(head.next)
    if head.next == None:
        print()

# 7. Delete the first k Nodes in a linked list using Recursion:

def del_kth_node(head,k):
    current = head
    if current == None:
        return None
    elif k == 0:
        return current
    elif k == 1:
        current = current.next
        return current
    elif k == 2:
        current.next = current.next.next
        return current
    else:
        current = del_kth_node(current.next,k-1)
        return current

# 9. Given a linked list, print alternate nodes of this linked list:

def print_alternate(head):
    if head == None:
        return None
    print(head.data,end="->")
    if head.next != None:
        print_alternate(head.next.next)
    else:
        print()
  

# 10. Given a doubly linked list. Reverse it using recursion. Here we assume, we keep self.head pointer. We are not keeping self.tail:

def reverse_dll_recursively(head):
    if head == None:
        return None
    
    temp = head.prev
    head.prev = head.next
    head.next = temp
    
    if head.prev == None:
        return head
    else:
        return reverse_dll_recursively(head.prev)

# 11. Write a recursive function minRec(self, n) to find the minimum element of a linked list, where n is the length of the linked list:

def min_rec(head,n):
    current = head
    if current == None:
        return None
    elif current.next == None or n == 1:
        return current.data
    if n == 0:
        return min_value
    min_value = min_rec(current.next,n-1)
    if current.data < min_value:
        return current.data
    else:
        return min_value

    
s = Singly_Linked_List()
s.add_node(3)
s.add_node(10)
s.add_node(45)
s.add_node(5)
s.add_node(1)
s.add_node(2)
s.add_node(8)
s.print_linked_list()
m = min_rec(s.head,10)
print(m)
