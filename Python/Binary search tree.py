class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def add_data(self,data):
        new_data = Node(data)
        if self.root == None:
            self.root = new_data
        else:
            prev = None
            current = self.root
            while current != None:
                if data < current.data:
                    prev = current
                    current = current.left
                    if current == None:
                        prev.left = new_data
                        break
                else:
                    prev = current
                    current = current.right
                    if current == None:
                        prev.right = new_data
                        break
                    
    def add(self,root,data):
        if root == None:
            return Node(data)
        if data < root.data:
            root.left = self.add(root.left,data)
        else:
            root.right = self.add(root.right,data)
        return root
                    
    def insert_r(self,data):
        self.root = self.add(self.root,data)
                        
    def print_inorder(self,t_root):
        if t_root == None:
            return
        self.print_inorder(t_root.left)
        print(t_root.data,end=" ")
        self.print_inorder(t_root.right)
        
    def find_max(self,root):
        current = self.root
        if root.right == None:
            print(root.data)
            return 
        self.find_max(root.right)
        
    def search(self,data):
        if self.root == None:
            print("empty")
        current = self.root
        while current != None:
            if current.data >= data:
                if current.data == data:
                    return True
                current = current.left
            else:
                if current.data == data:
                    return True
                current = current.right         
        return False
    
    def search_R(self,root,data):
        if self.root == None:
            return "empty"
        elif root == None:
            return False
        elif root.data == data:
            return True
        elif root.data >= data:
            return self.search(root.left,data)
        return self.search(root.right,data)  
        
    def find_min(self,root):
        if root.left == None:
            print(root.data)
            return 
        self.find_min(root.left)
        
    def print_preorder(self,root):
        if root == None:
            return
        print(root.data,end=" ")
        self.print_inorder(root.left)
        self.print_inorder(root.right)
        
    def print_postorder(self,root):
        if root == None:
            return
        self.print_inorder(root.left)
        self.print_inorder(root.right)
        print(root.data,end=" ")
    
    def max_even(self, root, max_v=0):
        if root is None:
            if max_v > 0:
                return max_v
            else:
                print("no even")
                return None  # Change this line to return None when there are no even values
        if root.data % 2 == 0 and root.data > max_v:
            max_v = root.data
        left_max = self.max_even(root.left, max_v)
        right_max = self.max_even(root.right, max_v)
        if left_max is not None and right_max is not None:
            return max(left_max, right_max)
        elif left_max is not None:
            return left_max
        else:
            return right_max

    # Assuming the rest of your BST class and methods are correctly implemented

             
t = BST()
t.add_data(25)
t.add_data(10)
t.add_data(35)
t.add_data(5)
t.add_data(20)
t.add_data(3)
t.add_data(6)
t.add_data(15)
t.add_data(21)
t.add_data(13)
t.add_data(40)
t.add_data(37)

t.print_inorder(t.root)
print()

s=t.max_even(t.root,0)
print(s)
# t.print_postorder(t.root)
# print()
# t.print_preorder(t.root)
# print()
# t.find_max(t.root)
# t.find_min(t.root)
# # s1 = t.search(2)
# s = t.search_R(t.root,3)
# # print(s1)
# print(s)
