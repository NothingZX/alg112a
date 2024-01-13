class PermutationGenerator:
    def __init__(self, data):
        self.data = list(data)
        self.length = len(data)
        self.result = []

    def generate_permutations(self):
        self._backtrack(0)
        return self.result

    def _backtrack(self, index):
        if index == self.length:
            self.result.append(tuple(self.data))
            return

        for i in range(index, self.length):
            self._swap(index, i)
            self._backtrack(index + 1)
            self._swap(index, i)  # Backtrack by swapping back

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

def main():
    # Example: Generate permutations for the string 'abc'
    input_string = 'abc'

    # Using custom PermutationGenerator class
    generator = PermutationGenerator(input_string)
    result = generator.generate_permutations()

    print(f"Permutations of '{input_string}':")
    for perm in result:
        print(''.join(perm))

if __name__ == "__main__":
    main()
