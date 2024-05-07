import lexBFS
import makegraph
import initial
import problem
import networkx as nx
import matplotlib.pyplot as plt

# Example graph
a=lexBFS.vertex('A',10,0)
b=lexBFS.vertex('B',10,1)
c=lexBFS.vertex('C',7,3)
d=lexBFS.vertex('D',4,4)
e=lexBFS.vertex('E',10,2)
f=lexBFS.vertex('F',1,6)
g=lexBFS.vertex('G',5,5)

graph1 = {
    a: [b],
    b: [a,c,f,g],
    c: [b,d,e,f],
    d: [c,e],
    e: [c,d,f],
    f: [b,c,e],
    g: [b]
}
graph2 = {
    a: [b],
    b: [a,c,f,g],
    c: [b,d,e],
    d: [c,e],
    e: [c,d,f],
    f: [b,e],
    g: [b]
}
#random graph
random = makegraph.num_vertices
graph3 = makegraph.make_graph(random)
# graph4 = makegraph.make_graph(random)

#scanf Random or Example graph
print("Chordal or Non_chordal or Random graph?: {Chordal/Non_chordal/Random} ")
graph = input()
check=True
while check:
    
    if graph == 'Chordal':
        graph=graph1
        check=False
    elif graph == 'Non_chordal':
        graph=graph2
        check=False
    elif graph == 'Random':
        graph=graph3
        check=False

    else :
        print("Choose from Chordal or Non_chordal or Random")
        print("Random or Example graph?: {Chordal/Non_chordal/Random} ")
        graph = input()


#1: lexicographic BFS
print("--------------------------------------------------------------------------------")
lexoBFS = lexBFS.lexbfs(graph)
visited_name=[]
for q in range(len(graph)):
    visited_name.append(lexoBFS[q].name)
print("The order from lexBFS is",  visited_name)

#2: recognizing chordal graph
print("--------------------------------------------------------------------------------")
problem.perfect(graph,lexoBFS)
print("Is the order perfect vertex elimination scheme?:",problem.perfect(graph,lexoBFS))


# if checking PEO function gives False, G is not chordal so cannot process
if problem.perfect(graph,lexoBFS)==False:
    print("This graph is not chordal/perfect")

if problem.perfect(graph,lexoBFS):

#3: Maximum weighted clique problem & Minimum graph colouring problem
    print("--------------------------------------------------------------------------------")
    problem.clique(graph,lexoBFS)

#4: Minimum clique cover problem
    print("--------------------------------------------------------------------------------")
    print("The minimum clique cover number is : ",problem.min_clique_cover(graph,lexoBFS))
    
#5: maximum weighted stabled set problem
    print("--------------------------------------------------------------------------------")
    problem.max_weighted_stabledset(graph,lexoBFS)



#drawing graph G=(V,E)
#--------------------------------------------------------------------------------------------
G = nx.Graph(graph)

# positions for all vertices
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

node_labels = {vertex: vertex.name+str(vertex.weight) for vertex in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=20, font_family='sans-serif')

plt.title("Graph Visualization")
plt.axis('off')  # Turn off the axis
plt.show()