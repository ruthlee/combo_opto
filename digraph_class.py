# goal: implement an adjacency list class for a digraph given a list of inputs that connect two vertices. 
# We want methods for adding edges by inputting two integers, i.e., 1, 2 means that vertices 1 and 2 are connected.
# since 

class edge:
    def __init__(self, v, w, weight):
        self.v = v 
        self.w = w
        self.weight = weight

class Digraph:
    ''' Note that the edge will always be represented in the adjacency list as a tuple with (end_vertex, weight).
    '''
    def __init__(self, V): # V is the number of vertices
        self.V = V
        self.adj_list = [[] for i in range(V)] # placeholder adjacency list 
    
    # add edge
    def add_edge(self, e): # v, w in V, we will add a tuple to the adjacency list. e is an instance of the edge class 
        if e.v > self.V or e.w > self.V: 
             raise ValueError('The vertex labels must be between ' + str(0) + ' and ' + str(self.V))
        self.adj_list[e.v].append((e.w, e.weight))
    
    def remove_edge(self, e):
        if e.v > self.V or e.w > self.V: 
             raise ValueError('The vertex labels must be between ' + str(0) + ' and ' + str(self.V))
        self.adj_list[e.v].remove((e.w, e.weight))
        
    def add_edges(self, edges):
        # takes in a list of edge instances and puts them in D. 
        for i in range(len(edges)):
            self.add_edge(edges[i])
    
    def remove_edges(self, edges):
        for i in range(len(edges)):
            self.remove_edge(edges[i])
            
    def print_digraph(self, long = False):
    # returns a summary of the digraph, with optional boolean input "long" for a more descriptive output
        if long: 
            for i in range(len(self.adj_list)):
                print('Vertex ' + str(i) + ' is adjacent to vertices ', end="")
                print(*self.adj_list[i])
        else:
            for i in range(len(self.adj_list)):
                print(str(i) + '->', end='')
                print(*self.adj_list[i], sep = '->')    
