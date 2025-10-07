from collections import deque
def create_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    
    for i in range(n):
        node = input(f"Enter name of node {i+1}: ")
        graph[node] = []
    
    e = int(input("Enter number of edges (paths): "))
    
    for i in range(e):
        src = input(f"Enter source node for edge {i+1}: ")
        dest = input(f"Enter destination node for edge {i+1}: ")
        
        if src in graph and dest in graph:
            try:
                cost = float(input(f"Enter cost for edge between {src} and {dest}: "))
                graph[src].append((dest, cost))
                graph[dest].append((src, cost))
            except ValueError:
                print("Invalid cost. Please enter a numeric value.")
        else:
            print(f"Error: One of the nodes '{src}' or '{dest}' does not exist.")
    
    return graph

def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        src = path[i]
        dest = path[i + 1]
        
        cost_found = False
        for neighbor, cost in graph[src]:
            if neighbor == dest:
                total_cost += cost
                cost_found = True
                break
        
        if not cost_found:
            print(f"No edge between {src} and {dest}. Cannot calculate total cost.")
            return None
    return total_cost

def main():
    print("===== Undirected Graph Creation ======")
    graph = create_graph()
    
    print("\n===== Graph Structure ======")
    for node, neighbors in graph.items():
        neighbor_str = ', '.join([f"{dest}(cost={cost})" for dest, cost in neighbors])
        print(f"{node} ---> [{neighbor_str}]")
    
    path_input = input("\nEnter the path (nodes separated by space) to calculate total cost: ")
    path = path_input.strip().split()
    
    cost = calculate_path_cost(graph, path)
    if cost is not None:
        # This line prints the total cost along the path
        print(f"\nTotal cost along the path {' -> '.join(path)}: {cost}")

main()
