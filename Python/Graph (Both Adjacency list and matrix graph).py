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
            
g = Graph(True)
# g.matrix_add("A")
# g.matrix_add("B")
# g.matrix_add("C")
# g.matrix_add("D")
# g.matrix_add("E")
# g.matrix_edge("A","B")
# g.matrix_edge("B","E")
# g.matrix_edge("A","C")
# g.matrix_edge("B","D")
# g.matrix_edge("C","D")
# g.matrix_edge("D","E")
# g.print_matrix()
# # g.matrix_node_del("C")
# g.matrix_edge_del("A","B")
# g.print_matrix()
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
# g.list_node_del("C")
g.list_edge_del("A","C",2)
g.print_list()