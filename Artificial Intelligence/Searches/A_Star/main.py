def init_start_goal(maze):
    for i in range(len(maze)):  # rows
        for j in range(len(maze[0])):  # columns
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    return start, goal


def get_neighbours(pos, maze):
    """Geting all valid neighbours of a position"""
    neighbours = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        x, y = pos[0] + dx, pos[1] + dy
        # check boundries
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
            neighbours.append(((x, y), 1))  # let costs is 1

    return neighbours


def heuristic(pos, goal):
    # Calculate the heuristic (Manhattan distance in this case)
    return manhattan_distance(pos, goal)


def manhattan_distance(pos1, pos2):
    # Calculate Manhattan distance between two positions
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def print_path(maze, path, cost):
    for step in path:
        row, col = step
        maze[row] = maze[row][:col] + 'X' + maze[row][col + 1:]

    for row in maze:
        print(row)
    print(f"Optimal Path Length: {len(path) - 1}")
    print(f"Total Cost: {cost}")


def ucs(maze):
    start, goal = init_start_goal(maze)
    visited = set()
    priority_queue = [(0, start, [])]  # tuple to store (cost, position, path)

    while priority_queue:
        priority_queue.sort()  # Sorting based on cost
        cost, current, path = priority_queue.pop(0)  # Pop min cost
        if current == goal:
            return path + [current], len(path) - 1  # concat path , steps taken

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours(current, maze)
        for neighbor, step_cost in neighbors:
            new_cost = cost + step_cost  # update cost and path
            new_path = path + [current]
            priority_queue.append((new_cost, neighbor, new_path))

    return [], None


def greedy_search(maze):
    start, goal = init_start_goal(maze)
    visited = set()
    # tuple to store (heuristic, position, path)
    priority_queue = [(heuristic(start, goal), start, [])]

    while priority_queue:
        priority_queue.sort()

        heuristics, current, path = priority_queue.pop(0)

        if current == goal:
            return path + [current], len(path) - 1

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours(current, maze)
        for neighbor, _ in neighbors:
            new_path = path + [current]
            priority_queue.append(
                (heuristic(neighbor, goal), neighbor, new_path))

    return [], None


def a_star(maze):
    start, goal = init_start_goal(maze)
    visited = set()
    # tuple to store (heuristic + cost, position, path)
    priority_queue = [(heuristic(start, goal), 0, start, [])]

    while priority_queue:
        priority_queue.sort()  # Sort based on the sum of heuristic and cost
        heuri, cost, current, path = priority_queue.pop(0)

        if current == goal:
            return path + [current], cost

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours(current, maze)
        for neighbor, step_cost in neighbors:
            new_cost = cost + step_cost
            new_path = path + [current]
            priority_queue.append(
                (new_cost + heuristic(neighbor, goal), new_cost, neighbor, new_path))

    return [], None


def main():

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

    path_a_star, cost_a_star = a_star(maze)

    path_ucs, cost_ucs = ucs(maze)

    path_greedy, cost_greedy = greedy_search(maze)

    print("\n=================\nRunning A*")
    print("Resultening maze: \n")
    if path_a_star:
        print_path(maze, path_a_star, cost_a_star)
    else:
        print("No path found for A*!")

    print("\n=================\nRunning UCS")
    print("Resultening maze: \n")
    if path_ucs:
        print_path(maze, path_ucs, cost_ucs)
    else:
        print("No path found for UCS!")

    print("\n=================\nRunning Greedy")
    print("Resultening maze: \n")
    if path_greedy:
        print_path(maze, path_greedy, cost_greedy)
    else:
        print("No path found for Greedy Search!")


main()
