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
            # Move Down
            new_node = swap_ele(curr_node, (row, col), (row + 1, col))
            if new_node not in visited:
                if (new_node == end):
                    break
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                queue.insert(0, new_node)

        if (row - 1) > -1:
            # Move Up
            new_node = swap_ele(curr_node, (row, col), (row - 1, col))
            if new_node not in visited:
                if (new_node == end):
                    break
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                queue.insert(0, new_node)

        if (col + 1) < 3:
            # Move Right
            new_node = swap_ele(curr_node, (row, col), (row, col + 1))
            if new_node not in visited:
                if (new_node == end):
                    break
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                queue.insert(0, new_node)

        if (col - 1) > -1:
            # Move Left
            new_node = swap_ele(curr_node, (row, col), (row, col - 1))
            if new_node not in visited:
                if (new_node == end):
                    break
                visited.append(new_node)
                parent_index.append(visited.index(curr_node))
                queue.insert(0, new_node)
    print('reached')
    print(end)
    print(curr_node)
    p_idx = 1
    while p_idx:
        idx = visited.index(curr_node)
        p_idx = parent_index[idx]
        print(visited[p_idx])
        curr_node = visited[p_idx]
    return 0, 0


if __name__ == '__main__':
    # start = [[1, 4, 7], [5, 0, 8], [2, 3, 6]]
    start = [[4, 7, 0], [1, 2, 8], [3, 5, 6]]

    goal = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]

    path, actions = BFS(start, goal)
