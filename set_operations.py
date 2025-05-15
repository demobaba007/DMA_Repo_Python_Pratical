class SET:
    def __init__(self, elements):
        self.elements = []
        for e in elements:
            if e not in self.elements:
                self.elements.append(e)

    def ismember(self, element):
        return element in self.elements

    def powerset(self):
        result = [[]]
        for elem in self.elements:
            result += [subset + [elem] for subset in result]
        return result

    def subset(self, other):
        for elem in self.elements:
            if elem not in other.elements:
                return False
        return True

    def set_union(self, other):
        result = self.elements[:]
        for elem in other.elements:
            if elem not in result:
                result.append(elem)
        return result

    def intersection(self, other):
        result = []
        for elem in self.elements:
            if elem in other.elements:
                result.append(elem)
        return result

    def complement(self, universal_set):
        result = []
        for elem in universal_set:
            if elem not in self.elements:
                result.append(elem)
        return result

    def set_difference(self, other):
        result = []
        for elem in self.elements:
            if elem not in other.elements:
                result.append(elem)
        return result

    def symmetric_difference(self, other):
        result = []
        for elem in self.elements:
            if elem not in other.elements:
                result.append(elem)
        for elem in other.elements:
            if elem not in self.elements:
                result.append(elem)
        return result

    def cartesian_product(self, other):
        result = []
        for a in self.elements:
            for b in other.elements:
                result.append((a, b))
        return result

    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}"


if __name__ == "__main__":
    elemsA = []
    elemsB = []
    universalSet = []
    n = int(input("Enter number of elements in Set A: "))
    print("Enter elements of Set A:")
    for _ in range(n):
        elemsA.append(int(input()))
    n = int(input("Enter number of elements in Set B: "))
    print("Enter elements of Set B:")
    for _ in range(n):
        elemsB.append(int(input()))
    n = int(input("Enter number of elements in Universal Set: "))
    print("Enter elements of Universal Set:")
    for _ in range(n):
        universalSet.append(int(input()))

    A = SET(elemsA)
    B = SET(elemsB)

    while True:
        print("\\nMenu:")
        print("1. Check if element is in Set A")
        print("2. Power set of Set A")
        print("3. Check if Set A is subset of Set B")
        print("4. Union of Set A and Set B")
        print("5. Intersection of Set A and Set B")
        print("6. Complement of Set A with respect to Universal Set")
        print("7. Set difference A - B")
        print("8. Symmetric difference of Set A and Set B")
        print("9. Cartesian product of Set A and Set B")
        print("10. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter element to check: "))
            print("Element is in Set A" if A.ismember(element) else "Element is not in Set A")
        elif choice == 2:
            print("Power set of Set A:")
            for subset in A.powerset():
                print(subset)
        elif choice == 3:
            print("Set A is a subset of Set B" if A.subset(B) else "Set A is not a subset of Set B")
        elif choice == 4:
            print("Union of Set A and Set B:", A.set_union(B))
        elif choice == 5:
            print("Intersection of Set A and Set B:", A.intersection(B))
        elif choice == 6:
            print("Complement of Set A with respect to Universal Set:", A.complement(universalSet))
        elif choice == 7:
            print("Set difference A - B:", A.set_difference(B))
        elif choice == 8:
            print("Symmetric difference of Set A and Set B:", A.symmetric_difference(B))
        elif choice == 9:
            print("Cartesian product of Set A and Set B:", A.cartesian_product(B))
        elif choice == 10:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
