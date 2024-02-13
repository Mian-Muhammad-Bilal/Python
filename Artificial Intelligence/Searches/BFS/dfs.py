# The dfs function is defined to perform Depth-First Search (DFS) on the maze. It takes the following parameters:

# maze: The maze represented as a 2D list of characters.
# start: The starting position in the maze (a tuple of (x, y) coordinates).
# goal: The goal position in the maze (a tuple of (x, y) coordinates).
# A stack, stack, is initialized to keep track of the current state and the path taken so far. Initially, it starts with the start position and an empty path.

# A set, visited, is initialized to keep track of visited positions to avoid revisiting the same position.

# The main loop runs while the stack is not empty. In each iteration, it pops the top state (position and path) from the stack.

# If the current position matches the goal position, the function returns the path, indicating that a path from the start to the goal has been found.

# If the current position has not been visited yet, it is marked as visited.

# The possible movements are defined as offsets in the x and y directions to go up, down, left, and right.

# For each possible movement, it calculates the new position (new_x, new_y) based on the current position and the movement.

# It checks if the new position is within the maze boundaries and if the position is not a wall ('#').

# If the new position is valid, it pushes the new state (new position and updated path) onto the stack for further exploration.

# If no path to the goal is found, the function returns an empty list.

# After defining the dfs function, the example maze is provided as a list of strings, and it is converted into a 2D list of characters.

# The code then searches for the start ('S') and goal ('G') positions in the maze.

# If both the start and goal positions are found, it calls the dfs function with the maze, start, and goal to find the path.

# If a path is found, it marks the path with 'X' in the maze and displays the maze with the optimal path, along with the length of the path and the total number of steps taken by the algorithm.

# If there is no path to the goal or if the start or goal positions are not found, appropriate messages are displayed.


def dfs(maze, start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path  # we reach the goal, return the path(saem as bfs)

        if (x, y) not in visited:
            visited.add((x, y))

            # movements
            movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for dx, dy in movements:
                new_x, new_y = x + dx, y + dy

                # Checking new position is valid and not visited

                if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
                    stack.append(((new_x, new_y), path + [(new_x, new_y)]))

    return []  # If path not found


maze = [
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

# Convert the maze intto nested list
maze = [list(row) for row in maze]

# Find the start and goal positions
start = None
goal = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

if start is not None and goal is not None:
    path = dfs(maze, start, goal)
    if path:
        # replacing 'dot' in the maze with 'X' to show the path in output
        for x, y in path:
            maze[x][y] = 'X'

        # Display the maze with the path
        for row in maze:
            print(''.join(row))
        print("Length of the optimal path:", len(path))
        print("Total number of steps taken by the algorithm:", len(path) - 1)
    else:
        print("No path to the goal.")
else:
    print("Start or goal not found in the maze.")
