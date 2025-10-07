from collections import deque
def create_graph():
    graph={}
    n=int(input("enter number of nodes:"))
    for i in range(n):
        node=input(f"enter name of node{i+1}:")
        graph[node]=[]
    e=int(input("enter number of edges(paths):"))

    for i in range(e):
        src=input(f"enter source node for edge{i+1}:")
        dest=input(f"enter destination node for edge{i+1}:")
        if src in graph and dest in graph:
            graph[src].append(dest)
        else:
            print(f"Error:One of the nodes '{src}' or '{dest}' does not exist")
    return graph

def dfs(graph,node,visited=None):
    if visited is None:
        visited=set()
    if node not in visited:
        print(f"visited:{node}")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(f"visited:{node}")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def main():
    print("=====Graph Creation======")
    graph=create_graph()
    print("=====Graph structure=======")
    for node,neighbors in graph.items():
        print(f"{node}--->{neighbors}")
    start=input("enter starting node for traversal:")
    if start not in graph:
        print("Invalid starting node")
        return
    print("=======DFS Traversal========")
    dfs(graph,start)
    print("=======BFS Traversal========")
    bfs(graph,start)

main()
