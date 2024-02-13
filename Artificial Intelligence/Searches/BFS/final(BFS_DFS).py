###BFS:

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

################################################################

###DFS:
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
