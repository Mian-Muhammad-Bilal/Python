import copy


def print_maze(maze):
    for row in maze:
        print(" ".join(row))


def compute_values(maze, policy, gamma=0.9, epsilon=0.01):
    rows, cols = len(maze), len(maze[0])
    values = [[0 for _ in range(cols)] for _ in range(rows)]

    while True:
        delta = 0
        temp_values = copy.deepcopy(values)

        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == 'G':
                    continue

                action = policy[i][j]
                if action == 'n':
                    next_i, next_j = i - 1, j
                elif action == 's':
                    next_i, next_j = i + 1, j
                elif action == 'e':
                    next_i, next_j = i, j + 1
                elif action == 'w':
                    next_i, next_j = i, j - 1

                next_i = max(0, min(next_i, rows - 1))
                next_j = max(0, min(next_j, cols - 1))

                reward = 10 if maze[next_i][next_j] == 'G' else 0
                temp_values[i][j] = reward + gamma * values[next_i][next_j]

                delta = max(delta, abs(temp_values[i][j] - values[i][j]))

        values = copy.deepcopy(temp_values)

        if delta < epsilon:
            break

    return values


def visualize_values(maze, values):
    rows, cols = len(maze), len(maze[0])

    print("Maze:")
    print_maze(maze)

    print("\nValues:")
    for i in range(rows):
        for j in range(cols):
            print(f"{values[i][j]:.2f}\t", end="")
        print()


if __name__ == "__main__":
    maze = [
        ['S', 'O', 'O', 'O', 'W', 'O', 'O', 'O', 'W', 'W'],
        ['O', 'W', 'O', 'W', 'O', 'W', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'W', 'O'],
        ['W', 'W', 'O', 'W', 'W', 'O', 'W', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'W', 'O'],
        ['O', 'W', 'O', 'W', 'O', 'W', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'O', 'O'],
        ['W', 'W', 'O', 'W', 'W', 'O', 'W', 'O', 'W', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'G', 'O'],
        ['W', 'W', 'W', 'O', 'O', 'O', 'W', 'W', 'O', 'O']
    ]

    policy = [
        ['e', 'e', 'e', 's', 'W', 'e', 'e', 'e', 'W', 'W'],
        ['n', 'W', 'n', 'W', 'n', 'W', 'n', 'e', 'e', 'e'],
        ['n', 'n', 'n', 's', 's', 's', 's', 'W', 'W', 's'],
        ['W', 'W', 's', 'W', 'W', 'e', 'W', 's', 's', 's'],
        ['s', 's', 's', 'e', 'e', 'e', 's', 'W', 'W', 's'],
        ['n', 'W', 'n', 'W', 'n', 'W', 's', 'e', 'e', 'e'],
        ['e', 'e', 'e', 's', 's', 's', 's', 'W', 'e', 's'],
        ['W', 'W', 's', 'W', 'W', 's', 'W', 'e', 'W', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'G', 'e'],
        ['W', 'W', 'W', 's', 's', 's', 'W', 'W', 's', 's']
    ]

    values = compute_values(maze, policy)
    visualize_values(maze, values)
