from queue import PriorityQueue

# Best First Search (using a priority queue)
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    
    while not pq.empty():
        _, current = pq.get()
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return
        
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
    
    print("\nGoal not reachable.")

# Example graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values (example)
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 0
}

# Run Best First Search
print("Path followed:")
best_first_search(graph, 'A', 'G', heuristic)
