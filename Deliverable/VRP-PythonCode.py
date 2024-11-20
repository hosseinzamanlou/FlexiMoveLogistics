# Import necessary libraries
import math
import matplotlib.pyplot as plt
from itertools import permutations

# ====================
# 1. Problem Setup
# ====================

# Define customer locations (Depot + Customers)
customer_locations = [(0, 0), (1, 3), (4, 4), (5, 1), (2, 5)]  # (x, y) coordinates
customer_demands = [0, 3, 4, 2, 5]  # Demands for each location (Depot has 0 demand)
truck_capacity = 10  # Maximum capacity per truck

# Distance matrix (computed later)
def calculate_distance_matrix(locations):
    n = len(locations)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((locations[i][0] - locations[j][0]) ** 2 +
                                          (locations[i][1] - locations[j][1]) ** 2)
    return dist_matrix

distance_matrix = calculate_distance_matrix(customer_locations)

# ====================
# 2. Nearest Neighbor Heuristic
# ====================

def nearest_neighbor_vrp(distance_matrix, customer_demands, truck_capacity):
    n_customers = len(customer_demands)
    visited = [False] * n_customers  # Track visited locations
    visited[0] = True  # Depot is always visited
    routes = []  # Final list of routes
    truck = []  # Current truck's route
    remaining_capacity = truck_capacity

    while not all(visited):
        current_location = truck[-1] if truck else 0  # Start from depot
        nearest_customer = None
        shortest_distance = float('inf')

        # Find the nearest unvisited customer
        for i in range(1, n_customers):
            if not visited[i] and customer_demands[i] <= remaining_capacity:
                if distance_matrix[current_location][i] < shortest_distance:
                    shortest_distance = distance_matrix[current_location][i]
                    nearest_customer = i

        if nearest_customer is None:
            # No more customers can be served with the current truck
            truck.append(0)  # Return to depot
            routes.append(truck)
            truck = []
            remaining_capacity = truck_capacity
        else:
            # Visit the nearest customer
            truck.append(nearest_customer)
            visited[nearest_customer] = True
            remaining_capacity -= customer_demands[nearest_customer]

    if truck:  # Add the final truck route
        truck.append(0)  # Return to depot
        routes.append(truck)

    return routes

routes_nn = nearest_neighbor_vrp(distance_matrix, customer_demands, truck_capacity)
print("Nearest Neighbor Routes:", routes_nn)

# ====================
# 3. Sweep Algorithm for Clustering
# ====================

def calculate_polar_coordinates(locations):
    polar_coordinates = []
    depot = locations[0]
    for i, (x, y) in enumerate(locations):
        angle = math.atan2(y - depot[1], x - depot[0]) * 180 / math.pi
        angle = angle if angle >= 0 else 360 + angle
        distance = math.sqrt((x - depot[0]) ** 2 + (y - depot[1]) ** 2)
        polar_coordinates.append((i, angle, distance))
    return sorted(polar_coordinates, key=lambda x: x[1])

polar_coordinates = calculate_polar_coordinates(customer_locations)

def sweep_algorithm(polar_coordinates, demands, capacity):
    clusters = []
    current_cluster = []
    current_load = 0

    for customer_id, angle, distance in polar_coordinates:
        if demands[customer_id] + current_load <= capacity:
            current_cluster.append(customer_id)
            current_load += demands[customer_id]
        else:
            clusters.append(current_cluster)
            current_cluster = [customer_id]
            current_load = demands[customer_id]

    if current_cluster:
        clusters.append(current_cluster)

    return clusters

clusters = sweep_algorithm(polar_coordinates, customer_demands, truck_capacity)
print("Clusters from Sweep Algorithm:", clusters)

# ====================
# 4. TSP Optimization Within Clusters
# ====================

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def solve_tsp(cluster, locations):
    depot = locations[0]
    min_route = None
    min_distance = float('inf')

    for perm in permutations(cluster):
        route = [0] + list(perm) + [0]
        distance = sum(calculate_distance(locations[route[i]], locations[route[i + 1]]) for i in range(len(route) - 1))
        if distance < min_distance:
            min_distance = distance
            min_route = route

    return min_route, min_distance

optimized_routes = []
for cluster in clusters:
    route, distance = solve_tsp(cluster, customer_locations)
    optimized_routes.append((route, distance))

print("Optimized Routes from Sweep and TSP:", optimized_routes)

# ====================
# 5. Visualization
# ====================

def visualize_routes(routes, locations, title="Optimized Routes"):
    plt.figure(figsize=(8, 6))
    for route, _ in routes:
        x = [locations[loc][0] for loc in route]
        y = [locations[loc][1] for loc in route]
        plt.plot(x, y, marker='o')
        for loc in route:
            plt.text(locations[loc][0], locations[loc][1], f'{loc}')
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

visualize_routes(optimized_routes, customer_locations, title="Optimized Routes Using Sweep and TSP")

# ====================
# 6. Evaluation Metrics
# ====================

def calculate_metrics(routes):
    total_distance = sum(route[1] for route in routes)
    num_trucks = len(routes)
    return {
        "Total Distance": total_distance,
        "Number of Trucks": num_trucks
    }

metrics = calculate_metrics(optimized_routes)
print("Evaluation Metrics:", metrics)
