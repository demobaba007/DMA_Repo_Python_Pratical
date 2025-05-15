def is_complete_graph(adj_matrix):
    n = len(adj_matrix)
    for i in range(n):
        for j in range(n):
            if i != j and adj_matrix[i][j] == 0:
                return False
    return True

def input_adjacency_matrix():
    while True:
        try:
            n = int(input("Enter the number of vertices in the graph: "))
            if n <= 0:
                print("Number of vertices must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("Enter the adjacency matrix row by row (0 or 1 values, separated by spaces):")
    adj_matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").strip().split()
            if len(row_input) != n:
                print(f"Please enter exactly {n} values.")
                continue
            try:
                row = [int(x) for x in row_input]
                if any(x not in (0, 1) for x in row):
                    print("Values must be 0 or 1.")
                    continue
                adj_matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter integers 0 or 1.")
    return adj_matrix

adj_matrix = input_adjacency_matrix()
if is_complete_graph(adj_matrix):
    print("The graph is a complete graph.")
else:
    print("The graph is NOT a complete graph.")