def ucs(maze):
    # Find the start and goal positions in the maze
    start, goal = init_start_goal(maze)
    # Set to keep track of visited positions
    visited = set()
    # Priority queue to store (cost, position, path) tuples
    priority_queue = [(0, start, [])]

    while priority_queue:
        # Sort the priority queue based on cost (UCS, so it's a regular sort)
        priority_queue.sort()
        # Pop the node with the minimum cost
        cost, current, path = priority_queue.pop(0)

        # If the current position is the goal, return the path and cost
        if current == goal:
            return path + [current], cost

        # Skip if the current position has already been visited
        if current in visited:
            continue

        # Mark the current position as visited
        visited.add(current)

        # Get neighbors of the current position
        neighbors = get_neighbuors(current, maze)
        for neighbor, step_cost in neighbors:
            new_cost = cost + step_cost
            new_path = path + [current]
            # Add the neighbor to the priority queue with updated cost and path
            priority_queue.append((new_cost, neighbor, new_path))

    # If no path is found, return an empty path and infinite cost
    return [], None


def init_start_goal(maze):
    # Loop through the maze to find the start and goal positions
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    return start, goal


def get_neighbuors(pos, maze):
    # Get valid neighbors of a position in the maze
    neighbuors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        x, y = pos[0] + dx, pos[1] + dy

        # Check if the neighbor is within bounds and is not a wall
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
            neighbuors.append(((x, y), 1))  # Assuming each step costs 1

    return neighbuors


# Example usage:
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

# Find the optimal path using UCS
path, cost = ucs(maze)

if path:
    # Mark the optimal path in the maze with 'X'
    for step in path:
        row, col = step
        maze[row] = maze[row][:col] + \
            'X' + maze[row][col + 1:]

    # Print the maze with the optimal path
    for row in maze:
        print(row)
    print(f"Optimal Path Length: {len(path) - 1}")
    print(f"Total Cost: {cost}")
else:
    print("No path found!")
