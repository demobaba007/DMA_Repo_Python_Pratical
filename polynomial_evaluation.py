def evaluate_polynomial(coeffs, n):
    result = 0
    degree = len(coeffs) - 1
    for i in range(degree + 1):
        result += coeffs[i] * (n ** i)
    return result


degree = int(input("Enter degree of polynomial: "))
print("Enter coefficients from constant term to highest degree term:")
coeffs = []
for _ in range(degree + 1):
    coeff = int(input())
    coeffs.append(coeff)
n = int(input("Enter value of n: "))
value = evaluate_polynomial(coeffs, n)
print(f"Value of polynomial at n = {n} is: {value}")
