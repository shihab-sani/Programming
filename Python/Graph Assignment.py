class Graph:
    def __init__(self,dir=False):
        self.dir = dir
        self.n = 0
        self.node = []
        self.list_graph = dict()
        self.matrix_graph = []
        
    def matrix_add(self,data):
        if data in self.node:
            print("Data already exists")
            return
        self.n += 1
        self.node.append(data)
        self.matrix_graph = [[0 for i in range(self.n)] for j in range(self.n)]
    
    def matrix_edge(self,st,ed,weight=None):
        if not self.node:
            print("graph is empty")
            return
        if st not in self.node or ed not in self.node:
            print("given data not found")
            return
        index_1 = self.node.index(st)
        index_2 = self.node.index(ed)
        if weight == None:
            self.matrix_graph[index_1][index_2] = 1
            if not self.dir:
                self.matrix_graph[index_2][index_1] = 1
        else:
            self.matrix_graph[index_1][index_2] = weight
            if not self.dir:
                self.matrix_graph[index_2][index_1] = weight
    
    def list_add(self,data):
        if data in self.list_graph:
            print("already exists")
            return
        self.list_graph[data] = []
        
    def list_edge(self,st,ed,weight=None):
        if not self.list_graph:
            print("graph is empty")
            return
        elif st not in self.list_graph or ed not in self.list_graph:
            print("given data not found")
            return
        if weight == None:
            self.list_graph[st].append(ed)
            if not self.dir:
                self.list_graph[ed].append(st)
        else:
            self.list_graph[st].append([ed,weight])
            if not self.dir:
                self.list_graph[ed].append([st,weight])
                
    def matrix_node_del(self,data):
        if data not in self.node:
            print("Data does not exists")
            return
        index = self.node.index(data)
        self.n -= 1
        self.node.remove(data)
        self.matrix_graph.pop(index)
        for i in self.matrix_graph:
            i.pop(index)
        
    def matrix_edge_del(self,st,ed):
        if not self.node:
            print("graph is empty")
            return
        if st not in self.node or ed not in self.node:
            print("given data not found")
            return
        
        index_1 = self.node.index(st)
        index_2 = self.node.index(ed)
        
        self.matrix_graph[index_1][index_2] = 0
        if not self.dir:
            self.matrix_graph[index_2][index_1] = 0
            
    def check_weight_list(self):
        for i in self.list_graph:
            l = self.list_graph[i]
            for j in l:
                if len(j) > 1:
                    return True
            return False
            
    def list_node_del(self,data):
        if data not in self.list_graph:
            print("Data does not exists")
            return 
        if self.check_weight_list():  
            self.list_graph.pop(data)
            for i in self.list_graph:
                l = self.list_graph[i]
                for j in l:
                    if data == j[0]:
                        l.remove(j)
                        break
        else:
            self.list_graph.pop(data)
            for i in self.list_graph:
                l = self.list_graph[i]
                if data in l:
                    l.remove(data)
        
    def list_edge_del(self,st,ed,weight=None):
        if not self.list_graph:
            print("graph is empty")
            return
        elif st not in self.list_graph or ed not in self.list_graph:
            print("given data not found")
            return
        if weight == None:
            if ed in self.list_graph[st]:
                self.list_graph[st].remove(ed)
                if not self.dir:
                    self.list_graph[ed].remove(st)
        else:
            temp_1 = [st,weight]
            temp_2 = [ed,weight]
            if temp_2 in self.list_graph[st]:
                self.list_graph[st].remove(temp_2)
                if not self.dir:
                    self.list_graph[ed].remove(temp_1) 
            
    def print_matrix(self):
        for i in range(self.n):
            print(self.node[i],":",self.matrix_graph[i])
        print()
            
    def print_list(self):
        for x in self.list_graph:
            print(x,":",self.list_graph[x])
        print()
        
def is_direct(graph):
    count = 0
    if isinstance(graph,dict):
        for i in graph:
            l = graph[i]
            for j in l:
                if i < j and i in graph[j]:
                    count += 1
    else:
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i < j and graph[i][j] == 1 and graph[j][i] == 1:
                    count += 1
    if count > len(graph):
        return False
    else:
        return True
            
# 1. Write a function to transform an adjacency list into an adjacency matrix.

def adj_list_to_matrix(adj_list):
    if not adj_list:
        print("list empty")
        return
    node = []
    for x in adj_list:
        node.append(x)
    adj_matrix = [[0] * len(node) for i in range(len(node))]
    for i in range(len(node)):
        for j in adj_list[node[i]]:
            index = node.index(j)
            adj_matrix[i][index] = 1
    for k in range(len(node)):
        print(node[k],":",adj_matrix[k])
        
# 2. Write a function to transform an adjacency matrix to an adjacency list.

def adj_matrix_to_list(adj_matrix):
    count = 0
    adj_list = dict()
    for i in range(len(adj_matrix)):
        adj_list[i] = []
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] >= 1:
                adj_list[i].append(j)
    for x in adj_list:
        print(x,":",adj_list[x])
        
# 3. Write a function to check if a given path exists in the grap or not. The
# function will take a list containing values as parameter and check if the path
# exists in the graph or not.
            
def path_exists(graph,path):
    if len(path) <= 1:
        print("no path entered")
        return
    for i in range(len(path)-1):
        curr = path[i]
        next = path[i+1]
        if isinstance(graph,dict):
            if next not in graph[curr]:
                return False
        else:
            if graph[curr][next] != 1:
                return False
    return True

# 4. Write a function to count the number of bidirectional edges in a directed
# graph. i.e for the above graph the output will be 1.

def bidirection_count(graph):
    count = 0
    if isinstance(graph,dict):
        for i in graph:
            l = graph[i]
            for j in l:
                if i < j and i in graph[j]:
                    count += 1
    else:
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i < j and graph[i][j] == 1 and graph[j][i] == 1:
                    count += 1
    return count

# 5. Write a global function to turn an directed graph into an undirected graph.

def direct_to_undirect(graph):
    if isinstance(graph,dict):
        for i in graph:
            l = graph[i]
            for j in l:
                if i not in graph[j]:
                    graph[j].append(i)
    else:
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] == 1 and graph[j][i] != 1:
                    graph[j][i] = 1

    return graph

# 6. Write a function to remove all the even nodes of a graph.

def even_node_del(graph):
    data = list(graph.keys())
    for i in data:
        if i%2==0:
            graph.pop(i)
    for j in graph:
        l = graph[j]
        for k in l:
            if k%2==0:
                l.remove(k)
    return graph

# 7. Write a function to remove only the bidirectional edges of a directed graph. If
# the graph does not contain any bidirectional edges print ‘No bidirectional
# edge found’

def del_bidirection(graph):
    found = False
    if isinstance(graph,dict):
        for i in graph:
            l = graph[i]
            for j in l:
                if i in graph[j]:
                    graph[j].remove(i)
                    found = True
    else:
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] == 1 and graph[j][i] == 1:
                    graph[j][i] = 0
                    found = True

    if not found:
        print("No bidirectional edge found")
        print()
        
# 8. Write a function to count the number of edges in a graph. The function work
# for both directed and undirected graph

def count_edges(graph):
    num_edges = 0
    if isinstance(graph,dict):
        for i in graph:
            num_edges += len(graph[i])
        if is_direct(graph):
            return num_edges
        else:
            num_edges = num_edges//2
            return num_edges
    else:
        for i in graph:
            for j in i:
                if j == 1:
                    num_edges += 1
        if is_direct(graph):
            return num_edges
        else:
            num_edges = num_edges//2
            return num_edges
        
# 9. Write a function to find the common adjacent nodes between three given nodes.

def com_adj(graph,adj_1,adj_2,adj_3):
    comm_adj = []
    if isinstance(graph,dict):
        lst_1 = graph[adj_1]
        lst_2 = graph[adj_2]
        lst_3 = graph[adj_3]
        for i in lst_1:
            if i in lst_2 and i in lst_3:
                comm_adj.append(i)
    else:
        lst_1 = graph[adj_1]
        lst_2 = graph[adj_2]
        lst_3 = graph[adj_3]
        for i in range(len(lst_1)):
            if lst_1[i] == 1 and lst_2[i] == 1 and lst_3[i] == 1:
                comm_adj.append(i)

    if not comm_adj:
        print("No common adjacent")
    else:
        print(comm_adj)
        
# 10. Write function souce_and_sink(matrix ) to print the source nodes and sink
# nodes in a graph where matrix is a adjacency matrix representation of a graph.

def source_and_sink(graph):
    source_node = []
    sink_node = []
    for i in range(len(graph)):
        sink = 0
        for j in range(len(graph)):
            sink += graph[i][j]
        if sink == 0:
            sink_node.append(i)

    for i in range(len(graph)):
        source = 0
        for j in range(len(graph)):
            source += graph[j][i]
        if source == 0:
            source_node.append(i)

    print(sink_node)
    print(source_node)
        
g = Graph(True)
g.matrix_add("A")
g.matrix_add("B")
g.matrix_add("C")
g.matrix_add("D")
g.matrix_add("E")
g.matrix_edge("A","B")
g.matrix_edge("B","E")
g.matrix_edge("A","C")
g.matrix_edge("B","D")
g.matrix_edge("C","D")
g.matrix_edge("D","E")
g.print_matrix()

g.list_add("A")
g.list_add("B")
g.list_add("C")
g.list_add("D")
g.list_add("E")
g.list_edge("A","B",5)
g.list_edge("B","E",7)
g.list_edge("A","C",2)
g.list_edge("B","D",4)
g.list_edge("C","D",9)
g.list_edge("D","E",3)
g.print_list()