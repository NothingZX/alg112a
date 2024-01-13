import time

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    start_time = time.time()

    def fib_recursive_helper(k, sequence=None):
        if sequence is None:
            sequence = []

        if k <= 0:
            return sequence
        elif k == 1:
            return sequence + [0]
        elif k == 2:
            return sequence + [0, 1]

        if len(sequence) < 2:
            sequence.extend([0, 1])

        next_fib = sequence[-1] + sequence[-2]
        return fib_recursive_helper(k-1, sequence + [next_fib])

    result = fib_recursive_helper(n)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Computed Fibonacci({n}) in {elapsed_time:.6f} seconds")

    return result

# Example: Print the first 10 Fibonacci numbers and measure time
result = fibonacci_recursive(10)
print(result)
