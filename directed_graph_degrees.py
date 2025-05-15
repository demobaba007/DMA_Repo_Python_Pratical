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
                # Remove duplicates if any
                neighbors = list(set(neighbors))
                adj_list[i] = neighbors
                break
            except ValueError:
                print("Invalid input. Please enter integers separated by spaces.")
    return adj_list

def compute_degrees(adj_list):
    n = len(adj_list)
    in_degrees = {v: 0 for v in adj_list}
    out_degrees = {v: len(adj_list[v]) for v in adj_list}
    
    for v in adj_list:
        for neighbor in adj_list[v]:
            in_degrees[neighbor] += 1
    
    return in_degrees, out_degrees

adj_list = input_adjacency_list()
in_degrees, out_degrees = compute_degrees(adj_list)

print("\nVertex\tIn-Degree\tOut-Degree")
for v in sorted(adj_list.keys()):
    print(f"{v}\t{in_degrees[v]}\t\t{out_degrees[v]}")
