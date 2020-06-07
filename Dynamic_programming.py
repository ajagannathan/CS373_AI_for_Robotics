# Dynamic Programming implemnetation
# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
import time
grid1 = [[0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0]]

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0]]

# goal = [len(grid)-1, len(grid[0])-1]
goal = [5, 3]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


# def setVal(node, closed, value, cost):
#     while(len(nodes) != 0):
#         for action in delta:
#             r = node[0] + action[0]
#             c = node[1] + action[1]
#             if(r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
#                 if(grid[r][c] != 1 and closed[r][c] != 'x'):
#                     closed[r][c] = 'x'
#                     value[r][c] = value[node[0]][node[1]] + cost

def show(arr):
    for i in range(len(arr)):
        print(arr[i])


def optimum_policy(grid, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2

    return value


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for i in range(len(grid[0]))] for j in range(len(grid))]
    closed = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    closed[goal[0]][goal[1]] = 'x'
    nodes = [goal]
    while(len(nodes) != 0):
        coord = nodes.pop(0)

        for action in delta:
            r = coord[0] + action[0]
            c = coord[1] + action[1]
            if(r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
                if(grid[r][c] != 1 and closed[r][c] != 'x'):
                    nodes.append([r, c])
                    closed[r][c] = 'x'
                    value[r][c] = value[coord[0]][coord[1]] + cost

    # TODO optimum policy
    show(value)

    weights = []
    closed[goal[0]][goal[1]] = '*'
    for i in range(len(closed)):
        for j in range(len(closed[0])):
            # if([i, j] == goal):
            #     closed[i][j] = '*'
            if(closed[i][j] != ' ' and closed[i][j] != '*'):
                for action in delta:
                    r = i + action[0]
                    c = j + action[1]
                    if(r >= 0 and r < len(closed) and c >= 0 and c < len(closed[0])):
                        if(closed[r][c] != ' '):
                            weights.append([value[r][c], r, c])
                if(len(weights) != 0):
                    weights.sort()
                    id_x, id_y = weights[0][1],  weights[0][2]
                    closed[i][j] = delta_name[delta.index(
                        [id_x - i, id_y - j])]
                    weights *= 0

    return closed


start_time = time.time()
show(compute_value(grid, goal, cost))
print("\n time : ", (time.time() - start_time))
