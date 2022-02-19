# Solution
# Copyright (c) 2022 Rishabh Mukund
# MIT License
#
# Description: Example code to use 8-puzzle-problem library to solve the
#              problem

import copy


def swap_ele(mat, pos1, pos2):
    """
    Definition
    ---
    Method to swap elements of a node from pos1 to pos2

    Parameters
    ---
    mat : Node of which the elements are to be swapped
    pos1, pos2: Positions of the elements to be swapped

    Returns
    ---
    mat1 : New node after swapping the elements
    """
    mat1 = copy.deepcopy(mat)
    mat1[pos1[0]][pos1[1]] = mat[pos2[0]][pos2[1]]
    mat1[pos2[0]][pos2[1]] = mat[pos1[0]][pos1[1]]
    return mat1


def position(x, arr):
    """
    Definition
    ---
    To get the row and coloumn of an element in a 2D list

    Parameters
    ---
    x : Element to be searched
    arr : 2D list

    Returns
    ---
    row, col : indices of the row and coloumn
    """
    for i in arr:
        if x in i:
            return arr.index(i), i.index(x)
    print("Error: Zero not found in node")
    return -1, -1


def BFS(init, end):
    """
    Definition
    ---
    A method to perform breath first search starting from initial node to the
    end node

    Parameters
    ---
    init : Node to start the BFS from
    end : Traget Node

    Returns
    ---
    Visited : A list of all the visited nodes in order
    parent_index : A list of parent indices for elements stored in visited
    """
    visited = [init]
    queue = [init]
    parent_index = [0]
    flag = False

    while queue:
        curr_node = queue.pop()
        row, col = position(0, curr_node)

        if (row + 1) < 3:
            # Move Up
            new_node = swap_ele(curr_node, (row, col), (row + 1, col))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

        if (row - 1) > -1:
            # Move Down
            new_node = swap_ele(curr_node, (row, col), (row - 1, col))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

        if (col + 1) < 3:
            # Move Left
            new_node = swap_ele(curr_node, (row, col), (row, col + 1))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

        if (col - 1) > -1:
            # Move Right
            new_node = swap_ele(curr_node, (row, col), (row, col - 1))
            if new_node not in visited:
                visited.append(new_node)
                parent_index.append(visited.index(curr_node) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

    if(flag):
        print('Path Found, Please check the generated text files')
        return visited, parent_index

    print('Error: No solution Exists for given start and end point')
    return -1, -1


def backtracking(visited, parent_index):
    """
    Definition
    ---
    Method to find path from solution of BFS

    Parameters
    ---
    Visited : A list of all the visited nodes in order
    parent_index : A list of parent indices for elements stored in visited

    Returns
    ---
    path : Path of nodes from start to end
    """
    curr_node = visited[-1]
    path = []
    p_idx = 1
    while p_idx:
        path.append(curr_node)
        p_idx = parent_index[visited.index(curr_node) - 1]
        curr_node = visited[p_idx]
    path.append(curr_node)
    return path[::-1]


if __name__ == '__main__':
    # Starting Node in the row wise format
    start = [[1, 0, 3], [4, 2, 5], [7, 8, 6]]

    # Goal Node in the row wise format
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    visited, parent_index = BFS(start, goal)
    path = backtracking(visited, parent_index)

    # Writing results to text files
    with open('nodePath.txt', 'w') as f:
        for line in path:
            line = [[row[i] for row in line] for i in range(len(line[0]))]
            line = str(line).replace('[', '').replace(']', '').replace(',', '')
            f.write(line + '\n')

    with open('Nodes.txt', 'w') as f:
        for line in visited:
            line = [[row[i] for row in line] for i in range(len(line[0]))]
            line = str(line).replace('[', '').replace(']', '').replace(',', '')
            f.write(line + '\n')

    with open('NodesInfo.txt', 'w') as f:
        for i in range(len(visited)):
            line = str(i + 1) + ' ' + str(parent_index[i]) + " 0"
            f.write(line + '\n')
