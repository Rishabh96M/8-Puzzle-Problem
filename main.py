# Solution
# Copyright (c) 2022 Rishabh Mukund
# MIT License
#
# Description: Example code to use 8-puzzle-problem library to solve the
#              problem

import copy


def swap_ele(mat, pos1, pos2):
    mat1 = copy.deepcopy(mat)
    mat1[pos1[0]][pos1[1]] = mat[pos2[0]][pos2[1]]
    mat1[pos2[0]][pos2[1]] = mat[pos1[0]][pos1[1]]
    return mat1


def position(x, arr):
    for i in arr:
        if x in i:
            return arr.index(i), i.index(x)


def BFS(init, end):
    visited = [init]
    queue = [init]
    parent_index = [0]

    while queue:
        curr_node = queue.pop()
        row, col = position(0, curr_node)

        if (row + 1) < 3:
            # Move Up
            new_node = swap_ele(curr_node, (row, col), (row + 1, col))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                if (new_node == end):
                    break
                queue.insert(0, new_node)

        if (row - 1) > -1:
            # Move Down
            new_node = swap_ele(curr_node, (row, col), (row - 1, col))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                if (new_node == end):
                    break
                queue.insert(0, new_node)

        if (col + 1) < 3:
            # Move Left
            new_node = swap_ele(curr_node, (row, col), (row, col + 1))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                if (new_node == end):
                    break
                queue.insert(0, new_node)

        if (col - 1) > -1:
            # Move Right
            new_node = swap_ele(curr_node, (row, col), (row, col - 1))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                if (new_node == end):
                    break
                queue.insert(0, new_node)

    print('reached')
    return visited, parent_index


def backtracking(visited, parent_index):
    curr_node = visited[-1]
    path = []
    p_idx = 1
    node_idx = []
    while p_idx:
        path.append(curr_node)
        node_idx.append(visited.index(curr_node))
        p_idx = parent_index[visited.index(curr_node)]
        curr_node = visited[p_idx]
    path.append(curr_node)
    print(path[::-1])
    print(node_idx[::-1])


if __name__ == '__main__':
    # start = [[1, 4, 7], [5, 0, 8], [2, 3, 6]]
    start = [[4, 7, 0], [1, 2, 8], [3, 5, 6]]

    goal = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]

    visited, parent_index = BFS(start, goal)
    backtracking(visited, parent_index)
