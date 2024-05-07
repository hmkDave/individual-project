import lexBFS
import initial
import random

class vertex:
    def __init__(self, name, weight, no):
        self.name = name
        self.weight = weight
        self.no = no


#get random |V| between 5 to 10
num_vertices = random.randint(5,26) # can change from here

#bring the alphabet
alpha = initial.alphabet()

#return random alphabet
def random_alpha():
    ra = random.choice(alpha)
    while ra not in alpha: # no same alphabet should be came out in graph
        ra = random.choice(alpha)
    alpha.remove(ra)
    return ra

#return random weight
def random_weight():  
    return random.choice(range(1, 10)) # random weight between from 1 to 5

#return random V
def vertices(ran_num):
    whole_vertex = [] # all vertices in graph

    for i in range(ran_num):
        ralp = random_alpha()
        m_address = id(ralp) # get address of ralp
        m_address = lexBFS.vertex(ralp,random_weight(),0) # apply new vertex
        whole_vertex.append(m_address)

    #after applying, sort them
    sort_vertices = initial.sorted_vertices(whole_vertex)
    
    #give them there own no
    no=0
    for vertex in sort_vertices:
        vertex.no=no
        no=no+1
    return sort_vertices

#adding edge
#connect two vertices (v1 and v2)
def add_edge(v1,v2,graph):
    # Check if vertex v1 is a valid vertex
    if v1 not in graph:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v2 is a valid vertex
    elif v2 not in graph:
        print("Vertex ", v2, " does not exist.")
    else:
        graph[v2].append(v1)
        graph[v1].append(v2)


#G=(V,E)
def make_graph(ran_num):
    graph={}
    vt = vertices(ran_num)
    for vertex in vt:
        graph[vertex] = []
    for ver1 in vt:
        for ver2 in vt:
            coin = [0,1]
            yorn = random.choice(coin)
            if ver1 == ver2:
                break
            if yorn == 1:
                add_edge(ver1,ver2,graph)
    return graph


