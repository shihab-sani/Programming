class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value

name = Node("Shehab Bin Islam")
id = Node(2320590)
major = Node("Computer Science")

name.next_node = id
id.next_node = major

a = name.get_next_node().get_value()
b = id.get_next_node().get_value()

print(a)
print(b)