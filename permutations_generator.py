def permute_without_repetition(digits, path, used, result):
    if len(path) == len(digits):
        result.append(''.join(path))
        return
    for i in range(len(digits)):
        if not used[i]:
            used[i] = True
            path.append(digits[i])
            permute_without_repetition(digits, path, used, result)
            path.pop()
            used[i] = False

def permute_with_repetition(digits, path, length, result):
    if len(path) == length:
        result.append(''.join(path))
        return
    for d in digits:
        path.append(d)
        permute_with_repetition(digits, path, length, result)
        path.pop()


digits = input("Enter the digits (e.g. 123): ")
rep_input = input("Allow repetition? (yes/no): ").strip().lower()
allow_repetition = rep_input == 'yes'

result = []
if allow_repetition:
    permute_with_repetition(list(digits), [], len(digits), result)
else:
    permute_without_repetition(list(digits), [], [False]*len(digits), result)

print(f"Generated {len(result)} permutations:")
for perm in result:
    print(perm)
