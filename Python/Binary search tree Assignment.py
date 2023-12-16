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

    def inorder(self):
        if self.root == None:
            print("Tree empty")
            return
        s = []
        current = self.root
        while current != None or len(s) != 0:
            while current != None:
                s.append(current)
                current = current.left
            current = s.pop()
            print(current.data,end="->")
            current = current.right
        print()
        
# 1. Write a function to print the deepest leaf nodes of a BST.

def deepest_leaf_nodes(root):
    if root is None:
        return []
    q = [root]
    res = []
    while q:
        lev = []
        for i in range(len(q)):
            node = q.pop(0)
            lev.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    res = lev
    print(*res)

# 2. Write a function that will print the maximum width of a BST.

def max_width(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if len(result) < len(level):
            result = level
    print(*result)
    
# 3. Write a function to find the height of a node recursively in a BST.

def max_height(root):
    if root is None:
        return 0

    left_height = max_height(root.left)
    right_height = max_height(root.right)

    if left_height > right_height:
        return left_height+1
    else:
        return right_height+1

# 4. Write a function to find the depth of a node recursively in a BST.

def max_depth(root):
    if root is None:
        return 0

    left_height = max_depth(root.left)
    right_height = max_depth(root.right)

    if left_height > right_height:
        return left_height+1
    else:
        return right_height+1
    
# 5. Write a function that will print nodes for each level of a binary search tree recursively.

def print_nodes_level(root,level=1):
    if root == None:
        return
    print("Level->",level,":",root.data)
    print_nodes_level(root.left,level+1)
    print_nodes_level(root.right,level+1)
    
# 6. Write a function to delete a node from a BST

def delete_node(root,data):
    if root == None:
        return
    if root.data == data:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            curr = root.right
            while curr.left != None:
                curr = curr.left
            root.data = curr.data
            root.right = delete_node(root.right,curr.data)
    elif root.data > data:
        root.left = delete_node(root.left,data)
    elif root.data < data:
        root.right = delete_node(root.right,data)
    return root

# 7. Write a function ‘checkSiblings(root, node1,node2) that takes the root node
# and two more nodes (node1, node2). This function will return true if node1
# and node2 are siblings. Otherwise returns false.

def check_siblings(root,node_1,node_2):
    if root == None:
        print("tree empty")
        return
    curr = root
    prev = None
    while curr != None:
        if curr.data == node_1:
            if prev == None:
                return False
            else:
                if (prev.left.data == node_1 and prev.right.data == node_2) or (prev.left.data == node_2 and prev.right.data == node_1):
                    return True
                else:
                    return False
        prev = curr
        if curr.data > node_1:
            curr = curr.left
        else:
            curr = curr.right
    return False

# 8. Write a function to Find the kth smallest element in a BST.
# For example for the above tree: if k = 4, 4th smallest element will be 7

def kth_smallest(root,k):
    if root == None:
        print("Tree empty")
        return
    s = []
    r = []
    current = root
    while current != None or len(s) != 0:
        while current != None:
            s.append(current)
            current = current.left
        current = s.pop()
        r.append(current.data)
        current = current.right
    if len(r) >= k:
        print(r[k-1])
    else:
        print("out of range")
        
# 9. Write a function named print_ancestors that takes in a number, as a parameter
# denoting a node in a BST and prints all of its ancestors. If the node is not
# present in the tree, print “Node not found!”

def print_ancestors(root, data):
    if root == None:
        return False
    if root.data == data:
        return True
    left_side = print_ancestors(root.left, data)
    right_side = print_ancestors(root.right, data)
    if left_side or right_side:
        print(root.data, end=" ")
        return True
    return False

# 10. Write a function named print_successors that takes in a number, as a
# parameter denoting a node in a BST and prints all of its successors. If the
# node is not present in the tree, print “Node not found!”

def print_successors(root,data):
    if root == None:
        return False
    curr = root
    while curr != None:
        if curr.data == data:
            break
        elif curr.data > data:
            curr = curr.left
        else:
            curr = curr.right
    if curr == None:
        print("Node not found!")
    else:
        successors = []
        curr = curr.right
        while curr != None:
            successors.append(curr.data)
            curr = curr.left
        if not successors:
            print("No successors found")
        else:
            print(successors)

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
t.add_data(37)
t.add_data(40)
t.add_data(41)



