# Graph for adjacent list
class Graph:
    def __init__(self,dir=False):
        self.dir = dir
        self.graph = dict()
    
    def add_data(self,data):
        if data in self.graph:
            print("Given data already exists")
            return
        self.graph[data] = []
        
    def add_edges(self,st,ed,weight=None):
        if st not in self.graph or ed not in self.graph:
            print("Given data not found")
            return
        elif not self.graph:
            print("Graph is empty")
            return
        if not weight:
            self.graph[st].append(ed)
            if not self.dir:
                self.graph[ed].append(st)
        else:
            self.graph[st].append([ed,weight])
            if not self.dir:
                self.graph[ed].append([st,weight])
                
    def is_weighted(self):
        if not self.graph:
            print("Graph is empty")
            return False
        for i in self.graph:
            l = self.graph[i]
            if len(l[0]) > 1:
                return True
            return False
                
    def del_data(self,data):
        if not self.graph:
            print("Graph is empty")
        if data not in self.graph:
            print("Given data not found")
            return
        
        if self.is_weighted():
            self.graph.pop(data)
            for i in self.graph:
                l = self.graph[i]
                for j in l:
                    if data == j[0]:
                        l.remove(j)
                        break
        else:
            self.graph.pop(data)
            for i in self.graph:
                l = self.graph[i]
                if data in l:
                    l.remove(data)
                    
    def del_edges(self,st,ed,weight=None):
        if not self.graph:
            print("Graph is empty")
            return
        if st not in self.graph and ed not in self.graph:
            print("Given data not found")
            return
        if weight:
            temp_1 = [st,weight]
            temp_2 = [ed,weight]
            if temp_2 in self.graph[st]:
                self.graph[st].remove(temp_2)
                if not self.dir:
                    self.graph[ed].remove(temp_1)
        else:
            if ed in self.graph[st]:
                self.graph[st].remove(ed)
                if not self.dir:
                    self.graph[ed].remove(st)
                    
    def in_degree(self,data):
        if not self.graph:
            print("Graph is empty")
            return
        if data not in self.graph:
            print("Given data not found")
            return
        count = 0
        if not self.is_weighted():
            for i in self.graph:
                if data in self.graph[i]:
                    count += 1
        else:
            for i in self.graph:
                l = self.graph[i]
                for j in l:
                    if data in j[0]:
                        count += 1
        return count
    
    def out_degree(self,data):
        if not self.graph:
            print("Graph is empty")
            return
        if data not in self.graph:
            print("Given data not found")
            return
        return len(self.graph[data])
                      
    def print_graph(self):
        for i in self.graph:
            print(i,":",self.graph[i])
        print()
    
# 1. Please write a function findMaxInOutDegree(self) function to find the node with
# maximum outdegree and the node with max indegree
    
def max_in_out_degree(graph):
    g = graph.graph
    if not g:
        print("Graph is empty")
        return 
    items = list(g.keys())
    in_degrees = []
    out_degrees = []
    max_in = []
    max_out = []
    for x in g:
        in_degrees.append(graph.in_degree(x))
        out_degrees.append(graph.out_degree(x))
        
    max_1 = max(in_degrees)
    max_2 = max(out_degrees)
    
    for j, m in enumerate(in_degrees):
        if m == max_1:
            max_in.append(items[j])
            
    for k, n in enumerate(out_degrees):
        if n == max_2:
            max_out.append(items[k])

    print(*max_in)
    print(*max_out)       
    
# 2. Please write a function friendNodes(self, node 1, node2) to check whether the nodes,
# node1 and node 2 are friend or not.

def friend_nodes(graph,node_1,node_2):
    if not graph:
        print("Graph is empty")
        return 
    list_1 = graph[node_1]
    list_2 = graph[node_2]
    for i in list_1:
        if i in list_2:
            return True
    return False
    
# 3. Given a directed graph G with N nodes. You can use any graph
# representation to solve the following problems.

# 3(a). Write a function printSinkNodes that takes in a graph and finds out the
# sink nodes of the given graph.

def sink_nodes(graph):
    if not graph:
        print("Graph is empty")
        return 
    
    for x in graph:
        if len(graph[x]) == 0:
            print(x)
                
# 3(b). Write a function to find out the Node with more than 1 outdegree and less
# than 2 indegree.

def out_and_in(graph):
    g = graph.graph
    if not graph:
        print("Graph is empty")
        return 
    for x in g:
        in_degrees = graph.in_degree(x)
        out_degrees = graph.out_degree(x)
        if out_degrees > 1 and in_degrees < 2:
            print(x)
            
# 4. check whether the following is a path or not. If it is a path, check whether it is a simple path or cycle path.

def path_checker(graph,path):
    if not graph:
        print("Graph is empty")
        return 
    for i in range(len(path)-1):
        curr = path[i]
        next = path[i+1]
        if next not in graph[curr]:
            return False
    if path[0] == path[-1]:
        print("Cycle path")
    else:
        print("Simple path")

g = Graph()
g.add_data("A")
g.add_data("B")
g.add_data("C")
g.add_data("D")
g.add_data("E")
g.add_edges("A","B")
g.add_edges("B","E")
g.add_edges("A","C")
g.add_edges("B","D")
g.add_edges("C","D")
g.add_edges("D","E")
g.add_edges("E","A")
g.print_graph()
g.del_data("B")
g.del_edges("A","B")
g.print_graph()
n = g.in_degree("B")
print(n)
o = g.out_degree("B")
print(o)
max_in_out_degree(g)
print(friend_nodes(g.graph,"A","D"))
sink_nodes(g.graph)
out_and_in(g)
path_checker(g.graph,["A","B","E"])