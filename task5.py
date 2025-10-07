import numpy as np
import random

def ant_colony_tsp(distances, n_ants=10, n_iterations=50, alpha=1, beta=2, rho=0.5, Q=100):
    n_cities = len(distances)
    pheromone = np.ones((n_cities, n_cities))   
    best_cost = float("inf")
    best_path = None
    for _ in range(n_iterations):
        all_paths = []
        for ant in range(n_ants):
            path = [random.randint(0, n_cities-1)]
            while len(path) < n_cities:
                i = path[-1]
                probs = []
                for j in range(n_cities):
                    if j not in path:
                        tau = pheromone[i][j] ** alpha
                        eta = (1.0 / (distances[i][j] + 1e-10)) ** beta
                        probs.append((j, tau * eta))
                total = sum(p for _, p in probs)
                probs = [(j, p/total) for j, p in probs]
                next_city = random.choices([j for j,_ in probs], weights=[p for _,p in probs])[0]
                path.append(next_city)
            cost = sum(distances[path[i]][path[i+1]] for i in range(n_cities-1)) + distances[path[-1]][path[0]]
            all_paths.append((path, cost))
            if cost < best_cost:
                best_cost = cost
                best_path = path
        pheromone *= (1 - rho) 
        for path, cost in all_paths:
            deposit = Q / cost
            for i in range(n_cities-1):
                pheromone[path[i]][path[i+1]] += deposit
            pheromone[path[-1]][path[0]] += deposit   
    return best_path, best_cost
if __name__ == "__main__":
    distances = np.array([
        [0, 2, 9, 10, 7],
        [2, 0, 6, 4, 3],
        [9, 6, 0, 8, 5],
        [10, 4, 8, 0, 6],
        [7, 3, 5, 6, 0]
    ])

    best_path, best_cost = ant_colony_tsp(distances, n_ants=20, n_iterations=100, alpha=1, beta=3, rho=0.5)
    print("Best Path:", best_path)
    print("Best Cost:", best_cost)

