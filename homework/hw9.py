def solve_maze(maze, start, end):
    def dfs(current):
        nonlocal solved
        if current == end:
            solved = True
            return

        row, col = current
        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row][new_col]
                and maze[new_row][new_col] != '#'
            ):
                visited[new_row][new_col] = True
                path.append((new_row, new_col))
                dfs((new_row, new_col))
                if not solved:
                    path.pop()

    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = [start]
    solved = False
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    dfs(start)

    return path if solved else None

# Example maze
maze_example = [
    ['S', ' ', '#', ' ', ' '],
    ['#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#'],
    [' ', ' ', ' ', '#', 'E'],
]

start_point = (0, 0)
end_point = (4, 4)

# Solve the maze
solution_path = solve_maze(maze_example, start_point, end_point)

# Print the solved maze
if solution_path:
    for row in range(len(maze_example)):
        for col in range(len(maze_example[0])):
            if (row, col) == start_point:
                print('S', end=' ')
            elif (row, col) == end_point:
                print('E', end=' ')
            elif (row, col) in solution_path:
                print('.', end=' ')
            else:
                print(maze_example[row][col], end=' ')
        print()
else:
    print("No solution found.")
