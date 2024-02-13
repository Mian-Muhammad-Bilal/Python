def get_neighbors(pos, maze):
    # Get valid neighbors of a position in the maze
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        x, y = pos[0] + dx, pos[1] + dy

        # Check if the neighbor is within bounds and is not a wall
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
            neighbors.append(((x, y), 1))  # Assuming each step costs 1

    return neighbors


def heuristic(pos, goal):
    # Calculate the heuristic (Manhattan distance in this case)
    return manhattan_distance(pos, goal)


def manhattan_distance(pos1, pos2):
    # Calculate Manhattan distance between two positions
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def init_start_goal(maze):
    # Loop through the maze to find the start and goal positions
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    return start, goal


def a_star(maze):
    # Find the start and goal positions in the maze
    start, goal = init_start_goal(maze)
    # Set to keep track of visited positions
    visited = set()
    # Priority queue to store (heuristic + cost, position, path) tuples
    priority_queue = [(heuristic(start, goal), 0, start, [])]

    while priority_queue:
        # Sort the priority queue based on the sum of heuristic and cost (A*, so it's a regular sort)
        priority_queue.sort()
        # Pop the node with the minimum sum of heuristic and cost
        _, cost, current, path = priority_queue.pop(0)

        # If the current position is the goal, return the path and cost
        if current == goal:
            return path + [current], cost

        # Skip if the current position has already been visited
        if current in visited:
            continue

        # Mark the current position as visited
        visited.add(current)

        # Get neighbors of the current position
        neighbors = get_neighbors(current, maze)
        for neighbor, step_cost in neighbors:
            new_cost = cost + step_cost
            new_path = path + [current]
            # Add the neighbor to the priority queue with updated heuristic and cost
            priority_queue.append(
                (new_cost + heuristic(neighbor, goal), new_cost, neighbor, new_path))

    # If no path is found, return an empty path and None as cost
    return [], None
