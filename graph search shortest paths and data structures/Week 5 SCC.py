from collections import defaultdict


'''def dfs_loop (graph):
    global visited
    visited = []
    global data_set
    data_set = []
    global time
    time = 0
    for vertex in (1, range(875714+1)):
        if vertex not in visited:
            dfs(graph, vertex)'''

graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs (G, v):
    '''visited, stack = set(), [v]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(G[vertex] - visited)
    return visited'''
    if v not in visited:
        visited.append(v)
        for n in G[v]:
            dfs(G,n)
    return visited

'''if __name__ == "__main__":
    with open('SCC.txt') as file:
        #graph = defaultdict(list)
        graph = defaultdict(set)
        for line in file:
            v1, v2 = line.split()
            #graph[v1].append(v2)
            graph[v1].add(v2)
    #print(graph["1"])'''
visited = []
a = dfs(graph, "A")
print(a)

'''class SccFinder(object):
    def __init__(self, input_file):
        self.scc_list = []
        with open(input_file) as file:
            self.finish_order = []
            self._graph = {}
            for line in file:
                (from_v, to_v) = tuple(number for number in line.split())
                self._add_edge_to_graph(int(from_v), int(to_v))

    def _add_edge_to_graph(self, from_v, to_v):
        if from_v in self._graph:
            self._graph[from_v].append(to_v)
        else:
            self._graph[from_v] = [to_v]
        if to_v in self._graph:
            self._graph[to_v].append(-from_v)
        else:
            self._graph[to_v] = [-from_v]

    def compute_finish_times(self):
        visited_nodes, finished_nodes = set(), set()
        for vertex in self._graph.keys():
            if vertex in visited_nodes:
                continue
            nodes_stack = [vertex]
            while nodes_stack:
                node = nodes_stack.pop()
                if node not in visited_nodes:
                    visited_nodes.add(node)
                    nodes_stack.append(node)
                    neighbors = (-edge for edge in self._graph[node] if edge < 0)
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            nodes_stack.append(neighbor)
                else:
                    if node not in finished_nodes:
                        self.finish_order.append(node)
                        finished_nodes.add(node)

    def compute_sccs(self):
        visited_nodes = set()
        assert (len(self.finish_order) == len(self._graph))
        for i in reversed(self.finish_order):
            if i in visited_nodes:
                continue
            nodes_stack = [i]
            size = 0
            while nodes_stack:
                node = nodes_stack.pop()
                if node not in visited_nodes:
                    size += 1
                    visited_nodes.add(node)
                    nodes_stack.append(node)
                    neighbors = (edge for edge in self._graph[node] if edge > 0)
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            nodes_stack.append(neighbor)
            self.scc_list.append(size)
        self.scc_list.sort(reverse=True)
        print(self.scc_list[:5])

if __name__ == "__main__":
    scc_finder = SccFinder("SCC.txt")
    scc_finder.compute_finish_times()
    scc_finder.compute_sccs()
    expected_sccs = [434821, 968, 459, 313, 211]
    print(scc_finder.scc_list[:5])'''