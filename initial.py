class vertex:
    def __init__(self, name, weight, no):
        self.name = name
        self.weight = weight
        self.no = no

#return alphabet
def alphabet():
    alpha= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return alpha

#to initialize the vertex
def init_vertex():
    null=vertex('NON',0,-100)
    return null

#checking if the graph has weight or not
def checking_weight(graph):
    if_weight_zero = 0 #if no weight =0, weighted =1
    for vertex in graph:
        if vertex.weight!=1:
            if_weight_zero=1
    return if_weight_zero

#find the first vertex to start
def first_vertex(graph):
    # started in alphabetical ascending order
    if_weight_zero = checking_weight(graph)

    #if no weighted graph, sorted with 
    if if_weight_zero ==0:
        sorted_graph = sorted(graph, key=lambda node:node.name, reverse=False)

    # started with maximum weighted vertex but if there are more than two, sort them in alphabetical order
    elif if_weight_zero ==1:
        sorted_graph = sorted(graph, key=lambda node:node.weight, reverse=True) #start from most weighted
        ama =1
        while ama:
            first_one_candidate = []
            first_one_candidate.append(sorted_graph[0])
            for ver_no in range(1, len(sorted_graph)):
                if sorted_graph[0].weight == sorted_graph[ver_no].weight:#if there are more than two vertices that have maximum weight
                    first_one_candidate.append(sorted_graph[ver_no])
                else : ama=0
        first_one_candidate = sorted(first_one_candidate, key=lambda node:node.name, reverse=False)#sort them in alphabetical order
        first_one = first_one_candidate[0]

    # if definition checking_weight returns number that is not 0 or 1  
    else :
        return print("error in the graph")
    
    # return start vertex and weighted or not
    return sorted_graph[0], if_weight_zero

#sort the random orderd vertices into right order (weighted and alphabetical order)
#ex) a(5),b(4),c(6),d(5),e(1),f(10),g(4) --> f(10),c(6),a(5),d(5),b(4),g(4),e(1)
def sorted_vertices(vertices):
    sorted_vertices = sorted(vertices, key=lambda node:node.weight, reverse=True)
    temp = sorted_vertices[0]
    q = [[] for _ in range(len(sorted_vertices))]
    i=0
    for vertex in sorted_vertices:
        
        if temp.weight == vertex.weight:
            q[i].append(vertex)
            temp = vertex
        else:
            temp=vertex
            i=i+1
            q[i].append(vertex)

    fin_sorted_vertices = []
    for j in range(i+1):
        q[j] = sorted(q[j], key=lambda node: node.name, reverse = False)
        fin_sorted_vertices = fin_sorted_vertices + q[j]
    return fin_sorted_vertices # cannot return the information of edge in graph

