# The bfs function is defined to perform Breadth-First Search (BFS) on the maze. It takes the same parameters as the dfs function:

# maze: The maze represented as a 2D list of characters.
# start: The starting position in the maze (a tuple of (x, y) coordinates).
# goal: The goal position in the maze (a tuple of (x, y) coordinates).
# A queue, queue, is initialized using a deque (double-ended queue) to keep track of the current state and the path taken so far. The starting position and an empty path are initially enqueued.

# A set, visited, is initialized to keep track of visited positions to avoid revisiting the same position.

# The main loop runs while the queue is not empty. In each iteration, it dequeues the front state (position and path).

# If the current position matches the goal position, the function returns the path, indicating that a path from the start to the goal has been found.

# If the current position has not been visited yet, it is marked as visited.

# The possible movements are defined as offsets in the x and y directions to go up, down, left, and right.

# For each possible movement, it calculates the new position (new_x, new_y) based on the current position and the movement.

# It checks if the new position is within the maze boundaries and if the position is not a wall ('#').

# If the new position is valid, it enqueues the new state (new position and updated path) for further exploration.

# If no path to the goal is found, the function returns an empty list.

# After defining the bfs function, the example maze is provided as a list of strings and is converted into a 2D list of characters.

# The code then searches for the start ('S') and goal ('G') positions in the maze.

# If both the start and goal positions are found, it calls the bfs function with the maze, start, and goal to find the path.

# If a path is found, it marks the path with 'X' in the maze and displays the maze with the optimal path, along with the length of the path and the total number of steps taken by the algorithm.

# If there is no path to the goal or if the start or goal positions are not found, appropriate messages are displayed.

from collections import deque


def bfs(maze, start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path  # If goal found then return the path

        if (x, y) not in visited:
            visited.add((x, y))

            # movements
            movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dx, dy in movements:
                new_x, new_y = x + dx, y + dy

                # Checking new position is valid and not visited
                if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
                    queue.append(((new_x, new_y), path + [(new_x, new_y)]))

    return []  # If no path found


maze = [
    "#############",
    "#S.........#",
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

# Convert the maze to a nested list
maze = [list(row) for row in maze]

# declairing the start and goal
start = None
goal = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

if start is not None and goal is not None:
    path = bfs(maze, start, goal)
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
