
from collections import deque
import initial
class vertex:
    def __init__(self, name, weight, no):
        self.name = name
        self.weight = weight
        self.no = no


# return the order of lexicographic order breast first search in backward
# used the algorithm from 84-85 pg the book ‘Algorithmic Graph Theory and Perfect Graphs’ by Martin Golumbic.
def lexbfs(graph):
    start, weighted= initial.first_vertex(graph) # start vertex
    visited = [initial.init_vertex() for _ in range(len(graph))] # put visited vertices
    wisited = [False for _ in range(len(graph))] # checking if the vertex is visited or not ex) if visited : True, if not : False

    label = [[] for _ in range(len(graph))]#assign the label null set to each vertex

    for i in range(len(graph)-1, -1, -1): # i from len(graph) to 1

        if i == len(graph)-1:# if for loop just started, assign the start vertex
            vertex=start
        else:
            label_strings = [''.join(map(str, sublist)) for sublist in label] # change list to string
            max_index = label_strings.index(max(label_strings)) # the location of maximum label vertex (label[max_index])
            
            while wisited[max_index]: # find the maximum label vertex until that vertex is not visited previously
                label_strings[max_index]=''
                max_index = label_strings.index(max(label_strings))
            vnum = label[max_index].pop(0) # pop the biggest number in label
            
            for v in graph: 
                if v.no == max_index:
                    vertex=v

        #if chosen vertex is not visited previously, put it into visited array and change to True 
        if vertex not in visited:
            visited[i] = vertex
            wisited[vertex.no] = True
        
        # give number to the neightbor
        for adj in graph[vertex]:
            if adj not in visited:
                label[adj.no].append(i)
    return visited
 


#A,B,C,
#   g h
#    V
# a--b--e
# |  |  |
# |  d  |
# |     |
# c-----f