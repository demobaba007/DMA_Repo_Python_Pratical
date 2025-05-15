def is_complete_graph(adj_list):
    vertices = list(adj_list.keys())
    n = len(vertices)
    for v in vertices:
        if len(adj_list[v]) != n - 1:
            return False
        for u in vertices:
            if u != v and u not in adj_list[v]:
                return False
    return True

def input_adjacency_list():
    while True:
        try:
            n = int(input("Enter the number of vertices in the graph: "))
            if n <= 0:
                print("Number of vertices must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    adj_list = {}
    print("Enter the adjacency list for each vertex.")
    print("For each vertex, enter the adjacent vertices separated by spaces.")
    print("Vertices should be labeled from 0 to", n-1)
    for i in range(n):
        while True:
            adj_input = input(f"Adjacency list for vertex {i}: ").strip().split()
            try:
                neighbors = list(map(int, adj_input))
                if any(neigh < 0 or neigh >= n for neigh in neighbors):
                    print(f"Vertices must be between 0 and {n-1}.")
                    continue
                neighbors = list(set(neighbors))
                adj_list[i] = neighbors
                break
            except ValueError:
                print("Invalid input. Please enter integers separated by spaces.")
    return adj_list

adj_list = input_adjacency_list()
if is_complete_graph(adj_list):
    print("The graph is a complete graph.")
else:
    print("The graph is NOT a complete graph.")