def find_solutions(n, C):
    solutions = []
    def backtrack(current, remaining, index):
        if index == n:
            if remaining == 0:
                solutions.append(current[:])
            return
        for value in range(remaining + 1):
            current.append(value)
            backtrack(current, remaining - value, index + 1)
            current.pop()

    backtrack([], C, 0)
    return solutions

def main():
    n = int(input("Enter the number of variables n: "))
    C = int(input("Enter the constant C (≤ 10): "))
    if C > 10:
        print("C should be less than or equal to 10.")
        return

    solutions = find_solutions(n, C)
    print(f"Found {len(solutions)} solutions:")
    for sol in solutions:
        print(sol)
main()
