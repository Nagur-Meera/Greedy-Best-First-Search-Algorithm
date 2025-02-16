# Greedy Best-First Search Algorithm

This repository demonstrates the implementation of a **Greedy Best-First Search Algorithm** using a graph and heuristic values in Python.

## Concept
The **Greedy Best-First Search Algorithm** is an informed search strategy that selects the next node based solely on its heuristic value. It aims to reach the goal as quickly as possible by expanding the node that appears to be the most promising (i.e., has the lowest heuristic value).

### Key Characteristics:
- Uses a heuristic function to estimate the cost from a node to the goal.
- Always selects the node with the minimum heuristic value.
- Does not guarantee finding the optimal path, but it is often faster in practice.
![image](https://github.com/user-attachments/assets/f7b34bbf-5877-4ca0-a9ed-3be3d00e7e97)

## Problem Representation
The graph used in this implementation is represented as an adjacency list:

```python
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': ['H'],
    'F': ['I', 'G'],
    'G': [],
    'H': [],
    'I': []
}
```

Each node also has a heuristic value representing the estimated cost from that node to the goal:

```python
heuristic = {
    'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8, 'F': 2, 'G': 0, 'H': 4, 'I': 9
}
```

## Algorithm Implementation
The core logic is as follows:

1. Start from the initial node.
2. Select the child node with the minimum heuristic value.
3. Move to the selected node.
4. Repeat the process until the goal node is reached or no further nodes are available.

### Python Code
```python
def find_min_heuristic(node):
    if not graph[node]:  
        return None  

    min_node = graph[node][0]
    min_value = heuristic[min_node]

    for child in graph[node]:
        if heuristic[child] < min_value:
            min_value = heuristic[child]
            min_node = child
    
    return min_node  

def greedy(start, goal):
    while True:
        print(start, end=' ')
        
        if start == goal:
            print("\nGoal is Reached")
            return
        
        next_node = find_min_heuristic(start)
        
        if next_node is None:  
            break
        
        start = next_node  
    
    print("\nGoal is not reached")

greedy('S', 'G')
```

## Output
```
S B F G
Goal is Reached
```

## How It Works
- Starts at node `S`.
- Chooses `B` because it has a lower heuristic value than `A`.
- Chooses `F` because it has a lower heuristic value than `E`.
- Chooses `G` because it has the lowest heuristic value (0), which is the goal node.

## Limitations
- Greedy Best-First Search is not guaranteed to find the shortest path.
- It can get stuck in local minima due to its reliance on heuristic values only.



