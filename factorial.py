def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
num = 5
print(f"The factorial of {num} is: {factorial(num)}")

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = 5
print(f"The factorial of {num} is: {factorial(num)}")

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
num_terms = 10
fib_sequence = fibonacci(num_terms)
print(f"The Fibonacci sequence up to {num_terms} terms is: {fib_sequence}")

a = 3
b = 4

a, b = b, a + b 

print(a)
print(b)