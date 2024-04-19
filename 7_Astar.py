import heapq

def is_valid(row, col, ROW, COL):
    return 0 <= row < ROW and 0 <= col < COL

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_destination(row, col, dest):
    return (row, col) == dest

def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

def trace_path(parents, dest):
    path = []
    while dest in parents:
        path.append(dest)
        dest = parents[dest]
    path.append(dest)
    return path[::-1]

def a_star_search(grid, src, dest):
    ROW, COL = len(grid), len(grid[0])
    if not (is_valid(src[0], src[1], ROW, COL) and is_valid(dest[0], dest[1], ROW, COL)):
        return "Source or destination is invalid"
    if not (is_unblocked(grid, src[0], src[1]) and is_unblocked(grid, dest[0], dest[1])):
        return "Source or the destination is blocked"

    closed_set = set()
    parents = {}
    open_list = [(0, src)]

    while open_list:
        f, (i, j) = heapq.heappop(open_list)
        if is_destination(i, j, dest):
            return ["The destination cell is found", trace_path(parents, dest)]
        closed_set.add((i, j))
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = i + dir[0], j + dir[1]
            if (is_valid(new_i, new_j, ROW, COL) and is_unblocked(grid, new_i, new_j) and 
                (new_i, new_j) not in closed_set):
                g_new = f + 1.0
                h_new = calculate_h_value(new_i, new_j, dest)
                f_new = g_new + h_new
                heapq.heappush(open_list, (f_new, (new_i, new_j)))
                parents[(new_i, new_j)] = (i, j)

    return "Failed to find the destination cell"

ROW, COL = 9, 10

grid = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
]
src, dest = (8, 0), (0, 0)

result = a_star_search(grid, src, dest)
if isinstance(result, list):
    print(result[0])
    print("The Path is ", "->".join(map(str, result[1])))
else:
    print(result)
