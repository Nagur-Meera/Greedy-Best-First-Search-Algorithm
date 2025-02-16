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

heuristic = {
    'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8, 'F': 2, 'G': 0, 'H': 4, 'I': 9
}

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