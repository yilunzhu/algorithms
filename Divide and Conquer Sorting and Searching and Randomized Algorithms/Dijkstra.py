def Dijkstra_path ():
    visited =[1]
    A[1] = 0
    while visited != V:
        length = []
        w_lst = []
        w_min = 0
        for vertex in visited:
            vertex = int(vertex)
            for edge in graph[vertex]:
                if int(edge[0]) not in visited:
                    w_lst.append(edge[0])
                    length.append(A[vertex] + int(edge[1]))
        w_min = int(w_lst[length.index(min(length))])
        A[w_min] = min(length)
        visited.append(w_min)
        visited.sort()


if __name__=="__main__":
    filename = 'dijkstraData.txt'
    V = []
    graph = {}
    with open(filename) as f:
        for line in f:
            l = line.split()
            V.append(int(l[0]))
            lst = []
            for edge in l[1:]:
                e = edge.split(",")
                lst.append([int(e[0]), e[1]])
            graph[int(l[0])] = lst
    #print(graph)
    #print(V)
    A = {}
    Dijkstra_path()
    lst = []
    print(A[7])
    print(A[37])
    print(A[59])
    print(A[82])
    print(A[99])
    print(A[115])
    print(A[133])
    print(A[165])
    print(A[188])
    print(A[197])
