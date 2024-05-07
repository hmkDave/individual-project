import initial

#True if list is a perfect vertex elimination scheme and False otherwise
#used the algorithm from 89-90 pg the book ‘Algorithmic Graph Theory and Perfect Graphs’ by Martin Golumbic.
def perfect(graph,list):
    A = [set() for _ in range(len(graph))] # for all vertices v do A(v) <- NULL
    for i in range(1,len(graph)-1): # from 1 to n-1
        v=list[i] # v = list(i)
        X=set() # X = adj(v) except the vertices that came out first than v from list 
        u = -1 # After the following for loop if u==-1, X is a empty set

        for adj in graph[v]:
            if list.index(v) < list.index(adj):
                X.add(adj)
                temp = list.index(adj)
                if u == -1 or u > temp:
                    u = temp
        X_t = X - {list[u]} # X — {u}

        A[u] = A[u] | X_t # concatenate X — {u} to A{u}

        test = [[] for _ in range(len(graph))] # array TEST of size n

        for w in graph[v]:
            w_num = list.index(w)
            test[w_num].append(1)

        for w in A[i]:
            w_num = list.index(w)
            if not test[w_num]:
                return False
            
        for w in graph[v]:
            w_num = list.index(w)
            test[w_num].append(1)
    return True

#used the algorithm from 98-100 pg the book ‘Algorithmic Graph Theory and Perfect Graphs’ by Martin Golumbic.
#input : adjacent sets of a chordal graph, perfect elimination scheme
#output : maximum weighted clique and chromatic number
def clique(graph, list):
    chromatic_num=1
    S = [0 for _ in range(len(list))]
    maximal_clique = [[] for _ in range(len(graph))]
    maximum_clique_weight = 0
    maximum_clique = []
    maximum_clique_name = []

    for i in range(len(graph)):
        v=list[i]
        v_num = i
        X=set() # X = adj(v) except the vertices that came out first than v from list
        u_num=-1 # After the following for loop if u==-1, X is a empty set

        for adj in graph[v]:
            if list.index(v) < list.index(adj):
                X.add(adj)
                temp = list.index(adj)
                if u_num==-1 or u_num > temp:
                    u_num=temp

        if len(graph[v])==0: # if Adj(v)=empty set
            print(v.name)

        if len(X)==0: # if X = empty set
            continue
        
        u = list[u_num] # u

        S[u_num] = max(S[u_num],len(X)-1) # S(u) = max(S(u),|X|-1)

        if S[v_num] < len(X): # if S(v) < |X| then do
            
            # print {v} union X
            X.add(v)
            maximal_clique[i] = X

            #chromatic number = max(chromatic number, 1+|X|)
            #As X add vertex v previously 1+|X| is len(X)
            chromatic_num = max(chromatic_num, len(X))

    # print maximum clique and chromatic number
    for clique in maximal_clique:
        total_weight=0
        if len(clique)==0:
            continue
        for vertex in clique:
            total_weight = total_weight + vertex.weight
        if maximum_clique_weight < total_weight:
            maximum_clique_weight = total_weight
            maximum_clique = clique
    for vertex in maximum_clique:
        maximum_clique_name.append(vertex.name)

    print("The maximum weighted clique is :", maximum_clique_name, "with weight of ", maximum_clique_weight)
    print("The chromatic number is ", chromatic_num)
    return maximum_clique,maximum_clique_weight


#input : adjacent set of chordal graph, perfect elimination scheme
#output : minimum clique cover number
#used the idea from 99 pg the book ‘Algorithmic Graph Theory and Perfect Graphs’ by Martin Golumbic.
def min_clique_cover(graph,list):
    y=[initial.init_vertex() for _ in range(len(list))]
    X=[set() for _ in range(len(list))]
    Y=[[] for _ in range(len(list))]
    total_X = set()
    y[0]=list[0]
    for adj in graph[y[0]]:
        if list.index(y[0])<list.index(adj):
            X[0].add(adj)
            total_X=total_X | X[0]

    Y[0]=X[0] | {y[0]}
    for i in range(1,len(list)):
        temp_y=set()
        y[i]=list[i]
        temp_y.add(y[i])
        if temp_y.isdisjoint(total_X)==False:
            y[i]=initial.init_vertex()
            continue

        for adj in graph[y[i]]:
            if list.index(y[i])<list.index(adj):
                X[i].add(adj)
                total_X = total_X | X[i]

        Y[i] = X[i].union({y[i]})
    num=0
    for t in Y:
        l=[]
        for v in t:
           l.append(v.name)
        if len(l)==0:
            continue
        num=num+1
        print(l)
    return num
    
#input : adjacent set of chordal graph, perfect elimination scheme
#output : maximum weighted stabled set
#used the algorithm from 'Some polynomial algorithms for certain graphs and hypergraphs' by Andras Frank.
def max_weighted_stabledset(graph,list):
    Red=[] 
    Blue=[]
    S=[vertex.weight for vertex in list] #array for weight order of list
    for i in range(len(list)):
        if S[i] <= 0:
            i=i+1
        else:
            Red.append(list[i])
            for adj in graph[list[i]]:
                j=list.index(adj)
                if i < j:
                    S[j] = S[j] - S[i]
                    if S[j] < 0:
                        S[j]=0
            S[i]=0
    Red.reverse()
    Blue_adj = set()
    for vertex in Red:
        if {vertex}.isdisjoint(Blue_adj):
            Blue.append(vertex)
            for adj in graph[vertex]:
                Blue_adj.add(adj)
    Blue_name=[]
    Blue_weight=0
    for vertex in Blue:
        Blue_name.append(vertex.name)
        Blue_weight=Blue_weight + vertex.weight
    print("The vertices of maximum weighted stabled set is :", Blue_name, "and The total weight is", Blue_weight)
    return Blue_name, Blue_weight
    
