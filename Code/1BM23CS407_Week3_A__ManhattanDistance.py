# Govind Jairam Rathod - 1BM23CS407
import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = [(x, y) for x in range(3) for y in range(3) 
                                   if goal[x][y] == state[i][j]][0]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    neighbors = []
    blank = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = blank

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print()

def astar_manhattan(start, goal):
    open_list = [(start, 0, [])]  # (state, g(n), path)
    visited = set()

    while open_list:
        current, g, path = open_list.pop(0)
        path = path + [current]

        if current == goal:
            print("Solution Found (Manhattan Distance):")
            for state in path:
                distance = manhattan_distance(state, goal)
                print(f"State: {state} | Manhattan Distance: {distance}")
            print_path(path)
            return g  # Return the depth (number of moves)

        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                h = manhattan_distance(neighbor, goal)
                open_list.append((neighbor, g + 1, path))

        open_list.sort(key=lambda x: x[1] + manhattan_distance(x[0], goal))

    return -1  # No solution found

# Example usage
start = [[2,8,3], [1,6,4], [7,0,5]]
goal = [[1,2,3], [8,0,4], [7,6,5]]
astar_manhattan(start, goal)
