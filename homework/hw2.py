def power_of_2_memoized(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    else:
        result = 2 * power_of_2_memoized(n - 1, memo)
        memo[n] = result
        return result

def main():
    # Get user input for the exponent
    while True:
        try:
            n = int(input("Enter the exponent (n) for 2^n: "))
            if n >= 0:
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Calculate and print 2^n using memoization
    result = power_of_2_memoized(n)
    print(f"2^{n} = {result}")

if __name__ == "__main__":
    main()
3