
""" Graph ADT, DFS/BFS and Dijkstra shortest path.

    Implements the graph as a map of (vertex,edge-map) pairs.
"""

#needed for searching using a stack
from stacks import Stack
from apq import *

import time

import os

import copy

######################################################################

class Vertex:
    """ A Vertex in a graph. """
    
    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __lt__(self, v):
        """ Return true if this object is less than v.
       
        Args:
            v -- a vertex object
        """
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element
    
######################################################################

class Edge:
    """ An edge in a graph.

    Implemented with an order, so can be used for directed or undirected
    graphs. Methods are provided for both. It is the job of the Graph class
    to handle them as directed or undirected.
    """
    
    def __init__(self, v, w, element):
        """ Create an edge between vertices v and w, with label element.

        Args:
            element -- the label, can be an arbitrarily complex structure.
        """
        self._vertices = (v,w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                   + str(self._vertices[1]) + ' : '
                   + str(self._element) + ')')

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element

######################################################################

class Graph:
    """ Represent a simple graph.

        This version maintains only undirected graphs, and assumes no
        self loops.
    """

    #Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the edge sets for that vertex
    #         Each edge set is also maintained as a dictionary,
    #         with opposite vertex as the key and the edge object as the value
    
    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr
    

    #--------------------------------------------------#
    #ADT methods to query the graph
    
    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])    #the dict of edges for v
        return num //2     #divide by 2, since each edge appears in the
                           #vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. 
        
        Beware - this method is inefficient, and will be really noticeable
        if used on large graphs.
        """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v.

        Args:
            v -- a vertex object
        """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None, if there is no edge.

        Args:
            v -- a Vertex object
            w -- a Vertex object
        """
        if (self._structure != None
                         and v in self._structure
                         and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    #--------------------------------------------------#
    #ADT methods to modify the graph
    
    def add_vertex(self, element):
        """ Add and return a new vertex with data element.

        Note -- if there is already a vertex with the same data element,
        this will create another vertex instance with the same element.
        If the client using this ADT implementation does not want these 
        duplicates, it is the client's responsibility not to add duplicates.
        """
        v = Vertex(element)
        self._structure[v] = dict()  # create an empty dict, ready for edges
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

        Checks for equality between the elements. If there is special
        meaning to parts of the element (e.g. element is a tuple, with an
        'id' in cell 0), then this method may create multiple vertices with
        the same 'id' if any other parts of element are different.

        To ensure vertices are unique for individual parts of element,
        separate methods need to be written.

        Beware -- this will be inefficient for large graphs.
        """
        for v in self._structure:
            if v.element() == element:
                #print('Already there')
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge, with element, between two vertices v and w.

        If either v or w are not vertices in the graph, does not add, and
        returns None.
            
        If an edge already exists between v and w, this will
        replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        # self._structure[v] is the dictionary of v's edges
        # so need to insert an entry for key w, with value e
        # A clearer way of expressing it would be
        # v_edges = self._structure[v]
        # v_edges[w] = e
        self._structure[v][w] = e  
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ Add all vertex pairs in elist as edges with empty elements. """
        for (v,w) in elist:
            self.add_edge(v,w,None)

    #--------------------------------------------------#
    #Additional methods to explore the graph
        
    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv            

    # --------------------------------------------------#
    # Traversal methods
    
    def dfs_stack(self, v):
        """ Return a DFS tree from v, using a stack.        """
        marked = {}
        stack = Stack()
        stack.push((v,None))
        # print('   pushed', v, 'from None')
        while stack.length() > 0:
            (vertex,edge) = stack.pop()
            if vertex not in marked:
                # print('popped unvisited', vertex)
                marked[vertex] = edge
                for e in self.get_edges(vertex):
                    w = e.opposite(vertex)
                    stack.push((w,e))
                    # print('   pushed', w, 'from', e)
        return marked

    def depthfirstsearch(self, v):
        """ Return a DFS tree from v. """
        marked = {v:None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        """ Do a recursive DFS from v, storing nodes in marked. """
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)
                
    def breadthfirstsearch(self, v):
        """ Return a BFS tree from v. """
        marked = {v:None}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = e
                        nextlevel.append(x)
            level = nextlevel
        return marked

    def BFS_length(self, v):
        """ Return a BFS tree from v, with path lengths. 
        
        In the returned dictionary, each vertex (key) stores its parent (value).
        """
        marked = {v:(None,0)}
        level = [v]
        levelint = 1
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = (w, levelint)
                        nextlevel.append(x)
            level = nextlevel
            levelint += 1
        return marked
    
    def breadthfirstsearchtree(self, v):
        """ Return a down-directed BFS tree from v. 
        
        In the returned dictionary, each vertex (key) stores a list of its edge 'children'.
        """
        marked = {v:[]}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = []
                        marked[w].append(x)
                        nextlevel.append(x)
            level = nextlevel
        return marked


    def dijkstra(self, s, d, APQType: bool):
        start = time.perf_counter()

        if d == None:
            print("no destination vertex given")

        if APQType == True:
            open = HeapAPQ()
        elif APQType == False:
            open = UnsortedAPQ()
        locs = {}
        closed = {}
        preds = {s: None}
        e = open.add(0, s)
        locs[s] = e
        totalCost = 0
        while open.length() > 0:
            ele = open.removeMin()
            cost = ele.getKey()
            vertex = ele.getValue()
            if vertex in locs:
                locs.pop(vertex)
            if vertex in preds:
                predecessor = preds.pop(vertex)
            closed[vertex] = (cost, predecessor)
            if d in closed and d != None:
                break
            for e in self.get_edges(vertex):
                w = e.opposite(vertex)
                if w not in closed:
                    newCost = cost + e.element()
                    if w not in locs:
                        preds[w] = vertex
                        ele = open.add(newCost, w)
                        locs[w] = ele
                    elif newCost < locs[w].getKey():
                        preds[w] = vertex
                        open.updateKey(locs[w], newCost)
        end = time.perf_counter()
        if APQType:
            if open.length() > 0:
                totalCost = open._heap[-1].getKey()
        runtime = end - start

        return closed, runtime, totalCost
    
    #End of class definition

# graph reader method
def graphreader(filename):
    """
    Read and return the route map in filename.
    """
    graph = Graph()
    file = open(os.getcwd()+filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph



######################################################################

def printResult(filename: str, source: int, destination, APQType: str):
    """
    Args:
        filename (str): path name of file to read
        source (int): source vertex
        destination (int/None): destination vertex
                                if none runs as normal
        APQType (bool): True for HeapAPQ, False for UnsortedAPQ
    """
    g = graphreader(filename)

    source = g.get_vertex_by_label(source)
    if destination != None:
        destination = g.get_vertex_by_label(destination)

    if APQType == 'HeapAPQ':
        type = True
    elif APQType == 'UnsortedAPQ':
        type = False
    
    d = g.dijkstra(source, destination, type)
    totalCost = 0
    if not type:
        totalCost = list(d[0].values())[-1][0]
    else:
        totalCost = d[2]
    for v in d[0]:
        print(f'\nVertex: {str(v)}\nCost from source:{str(d[0][v][0])}\nPredecessor: {str(d[0][v][1])}')

    print(f'\nTotal Cost: {totalCost}')

    print(f'\nRESULTS\nFile: {filename}\nSource: {source}\nDestination Vertex: {destination}\nAPQType: {APQType}\nRuntime: {d[1]}')

if __name__ == '__main__':
    printResult('simplegraph2.txt', 15, 14, 'UnsortedAPQ')