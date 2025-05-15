class RELATION:
    def __init__(self, matrix=None):
        self.matrix = matrix
        self.size = len(matrix) if matrix else 0

    def set_matrix(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if not self.matrix[i][i]:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j and self.matrix[i][j] and self.matrix[j][i]:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j]:
                    for k in range(self.size):
                        if self.matrix[j][k] and not self.matrix[i][k]:
                            return False
        return True

    def classify_relation(self):
        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        if reflexive and symmetric and transitive:
            return "Equivalence Relation"
        elif reflexive and antisymmetric and transitive:
            return "Partial Order Relation"
        else:
            return "None"

    def print_matrix(self):
        if not self.matrix:
            print("No relation matrix set.")
            return
        print("Relation Matrix:")
        for row in self.matrix:
            print(" ".join(str(int(x)) for x in row))


def input_matrix():
    while True:
        n = int(input("Enter the size of the square relation matrix: "))
        print(f"Enter the relation matrix ({n} rows of {n} elements each, 0 or 1):")
        matrix = []
        valid = True
        for i in range(n):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != n or any(x not in (0, 1) for x in row):
                print(f"Invalid input in row {i+1}. Each row must have exactly {n} elements of 0 or 1.")
                valid = False
                break
            matrix.append([bool(x) for x in row])
        if valid:
            return matrix
        else:
            print("Please re-enter the entire matrix correctly.\n")



relation = RELATION()
while True:
    print("\nMenu:")
    print("1. Input relation matrix")
    print("2. Print relation matrix")
    print("3. Check if Reflexive")
    print("4. Check if Symmetric")
    print("5. Check if Anti-symmetric")
    print("6. Check if Transitive")
    print("7. Classify relation")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        matrix = input_matrix()
        relation.set_matrix(matrix)
    elif choice == '2':
        relation.print_matrix()
    elif choice == '3':
        if relation.size == 0:
            print("Please input the relation matrix first.")
        else:
            print("Reflexive:", "Yes" if relation.is_reflexive() else "No")
    elif choice == '4':
        if relation.size == 0:
            print("Please input the relation matrix first.")
        else:
            print("Symmetric:", "Yes" if relation.is_symmetric() else "No")
    elif choice == '5':
        if relation.size == 0:
            print("Please input the relation matrix first.")
        else:
            print("Anti-symmetric:", "Yes" if relation.is_antisymmetric() else "No")
    elif choice == '6':
        if relation.size == 0:
            print("Please input the relation matrix first.")
        else:
            print("Transitive:", "Yes" if relation.is_transitive() else "No")
    elif choice == '7':
        if relation.size == 0:
            print("Please input the relation matrix first.")
        else:
            print("Classification:", relation.classify_relation())
    elif choice == '8':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")