def print_maze(maze):
    for row in maze:
        print(" ".join(row))


def print_computed_values(maze, values):
    rows, cols = len(maze), len(maze[0])

    print_maze(maze)
    print('\nCalculated values for each index in the given maze: \n')
    for i in range(rows):
        for j in range(cols):
            print(f"{values[i][j]:.2f}\t", end="")


def value_computation(maze, policy, gamma=0.9):
    rows, cols = len(maze), len(maze[0])
    # Initialize all maze indexes to 0
    values = [[0 for _ in range(cols)] for _ in range(rows)]

    while True:
        # Initialize change in values for convergence check
        delta = 0

        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == 'G':
                    continue  # Skip goal state as it has no further actions

                # Determine the next state based on the current policy
                action = policy[i][j]
                if action == 'n':
                    new_i, new_j = i - 1, j
                elif action == 's':
                    new_i, new_j = i + 1, j
                elif action == 'e':
                    new_i, new_j = i, j + 1
                elif action == 'w':
                    new_i, new_j = i, j - 1

                # Ensure the next position is within bounds
                new_i = max(0, min(new_i, rows - 1))
                new_j = max(0, min(new_j, cols - 1))

                # Reward for reaching the goal
                reward = 10 if maze[new_i][new_j] == 'G' else 0

                # Bellman equation for new values
                new_value = reward + gamma * values[new_i][new_j]

                # Update delta for convergence check
                delta = max(delta, abs(new_value - values[i][j]))
                values[i][j] = new_value

        if delta <= 0:  # revention from infnite loop
            break

    return values


def main():
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

    values = value_computation(maze, policy)
    print('\nGiven Maze: ')
    print_computed_values(maze, values)


if __name__ == "__main__":
    main()
