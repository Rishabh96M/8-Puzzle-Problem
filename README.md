[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Verified on python 3.8.10 and packages used are Copy and NumPy.

# 8-Puzzle-Problem
Solution to a 8-Puzzle-Problem using BFS and backtracking for the optimum solution.

## To install the dependencies
```
sudo pip install numpy
```

## Steps to run
To clone the file:
```
git clone https://github.com/rishabh96m/8-Puzzle-Problem.git
```
To run the code:
```
cd 8-Puzzle-Problem/
python3 main.py
```
The default start node is [[1, 0, 3], [4, 2, 5], [7, 8, 6]] and end node is [[1, 2, 3], [4, 5, 6], [7, 8, 0]] in row wise format. <br />
<br />
Row wise format Example:  [[1, 0, 3], [4, 2, 5], [7, 8, 6]] means the node is:<br />
1 0 3 <br />
4 2 5 <br />
7 8 6 <br />
<br />
To change the starting and ending node: open the main.py file in any editor, and change the start and end variables under the main function. Please make sure you follow row wise format like mentioned above.<br />
<br />
If a solution exists from start to end then Nodes.txt, NodesInfo.txt and nodePath.txt files will be generated in the current path of the program

## Steps to plot the Solution
After generating the 3 .txt files successfully from the above step, we can plot the solution using.
```
cd 8-Puzzle-Problem/
python3 plot_path.py
```

## Significance of Generated text files
### Nodes.txt
All the explored states present in the format of nodePath.txt

### NodesInfo.txt
First column: Node Index<br />
Second Column: Parent Node Index

### nodePath.txt
The elements are being stored column-wise, i.e. for this state 1 4 7 2 5 8 3 6 0, the eight puzzle state is <br />
1 2 3 <br />
4 5 5 <br />
7 8 0 <br />
The order of the states are from start node to the goal node.
