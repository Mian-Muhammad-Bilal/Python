def find_start_and_goal(maze):
    """Find the start and goal positions in the maze."""
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    return start, goal


def get_neighbors(maze, current):
    """Get valid neighboring cells for the current position."""
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for direction in directions:
        neighbor = (current[0] + direction[0], current[1] + direction[1])
        if is_valid(maze, neighbor):
            neighbors.append(neighbor)

    return neighbors


def is_valid(maze, cell):
    """Check if the cell is a valid and unblocked position in the maze."""
    rows, cols = len(maze), len(maze[0])
    return 0 <= cell[0] < rows and 0 <= cell[1] < cols and maze[cell[0]][cell[1]] != '#'


def manhattan_distance(point1, point2):
    """Calculate the Manhattan distance between two points."""
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def print_path(maze, path):
    """Print the maze with the optimal path marked as 'X'."""
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == path[0]:
                print('S', end=' ')
            elif (i, j) == path[-1]:
                print('G', end=' ')
            elif (i, j) in path:
                print('X', end=' ')
            else:
                print(maze[i][j], end=' ')
        print()


def greedy_search(maze):
    """Perform Greedy Search on the given maze."""
    start, goal = find_start_and_goal(maze)

    visited = set()
    path = []
    stack = [start]

    while stack:
        current = stack.pop()

        if current == goal:
            path.append(current)
            break  # Goal reached, exit the loop

        visited.add(current)
        neighbors = get_neighbors(maze, current)

        # Sort neighbors based on heuristic (Manhattan distance to the goal)
        neighbors.sort(key=lambda neighbor: manhattan_distance(
            neighbor, goal), reverse=True)
        # def custom_key_function(neighbor):
        #     return manhattan_distance(neighbor, goal)

        # neighbors.sort(key=custom_key_function, reverse=True)

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                path.append(current)
                break  # Move to the next iteration of the outer loop

    if path:
        print("Greedy Search Path:")
        print_path(maze, path)
    else:
        print("No path found to the goal.")


# Example Maze
maze_example = [
    "#############",
    "#S..........#",
    "#.###########",
    "#.#...#...#.#",
    "#.#.#.#.#.#.#",
    "#...#...#...#",
    "#.#.#.#.#.#.#",
    "#.#...#...#.#",
    "#.###########",
    "#....G......#",
    "#############"
]

# Perform Greedy Search on the example maze
greedy_search(maze_example)
