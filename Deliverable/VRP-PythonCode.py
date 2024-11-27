import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from itertools import permutations
import requests

# ====================
# Data Generation
# ====================
def generate_distance_matrix(num_locations):
    """Generate a symmetric distance matrix for locations."""
    distance_matrix = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(i + 1, num_locations):
            distance = random.randint(1, 50)  # Random distance
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

def generate_customer_demands(num_customers, max_demand=10):
    """Generate customer demand data."""
    demands = [{"CustomerID": f"Customer_{i}", "Demand": random.randint(1, max_demand)} for i in range(1, num_customers + 1)]
    demands.insert(0, {"CustomerID": "Depot", "Demand": 0})
    return pd.DataFrame(demands)

def generate_truck_capacities(num_trucks, max_capacity=15):
    """Generate truck capacity data."""
    capacities = [{"TruckID": f"Truck_{i}", "Capacity": random.randint(max_capacity - 5, max_capacity)} for i in range(1, num_trucks + 1)]
    return pd.DataFrame(capacities)

# ====================
# Visualization
# ====================
def visualize_routes(routes, coordinates):
    """Visualize routes on a 2D plane."""
    plt.figure(figsize=(10, 8))
    for route in routes:
        x = [coordinates[loc][0] for loc in route]
        y = [coordinates[loc][1] for loc in route]
        plt.plot(x, y, marker='o')
        for loc in route:
            plt.text(coordinates[loc][0], coordinates[loc][1], f'{loc}')
    plt.title("Optimized Delivery Routes")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid()
    plt.show()

# ====================
# Algorithms
# ====================
# 1. Nearest Neighbor Heuristic
def nearest_neighbor_vrp(distance_matrix, customer_demands, truck_capacity):
    n_customers = len(customer_demands)
    visited = [False] * n_customers
    visited[0] = True
    routes = []
    truck = []
    remaining_capacity = truck_capacity

    while not all(visited):
        current_location = truck[-1] if truck else 0
        nearest_customer = None
        shortest_distance = float('inf')

        for i in range(1, n_customers):
            if not visited[i] and customer_demands[i] <= remaining_capacity:
                if distance_matrix[current_location][i] < shortest_distance:
                    shortest_distance = distance_matrix[current_location][i]
                    nearest_customer = i

        if nearest_customer is None:
            truck.append(0)
            routes.append(truck)
            truck = []
            remaining_capacity = truck_capacity
        else:
            truck.append(nearest_customer)
            visited[nearest_customer] = True
            remaining_capacity -= customer_demands[nearest_customer]

    if truck:
        truck.append(0)
        routes.append(truck)

    return routes

# 2. Sweep Algorithm
def calculate_polar_coordinates(locations):
    """Convert Cartesian coordinates to polar coordinates."""
    polar_coordinates = []
    depot = locations[0]
    for i, (x, y) in enumerate(locations):
        angle = math.atan2(y - depot[1], x - depot[0]) * (180 / math.pi)
        angle = angle if angle >= 0 else 360 + angle
        distance = math.sqrt((x - depot[0]) ** 2 + (y - depot[1]) ** 2)
        polar_coordinates.append((i, angle, distance))
    return sorted(polar_coordinates, key=lambda x: x[1])

def sweep_algorithm(polar_coordinates, demands, capacity):
    """Cluster customers using the Sweep Algorithm."""
    clusters = []
    current_cluster = []
    current_load = 0

    for customer_id, angle, _ in polar_coordinates:
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

# 3. 2-Opt Algorithm
def two_opt(route, distance_matrix):
    """Optimize a route using 2-Opt."""
    best_distance = calculate_total_distance(route, distance_matrix)
    best_route = route
    improved = True

    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_distance = calculate_total_distance(new_route, distance_matrix)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_route = new_route
                    improved = True

    return best_route, best_distance

def calculate_total_distance(route, distance_matrix):
    """Calculate the total distance of a route."""
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# ====================
# Data Loading
# ====================
num_locations = 10
num_customers = 9
num_trucks = 3

# Generate synthetic data
distance_matrix = generate_distance_matrix(num_locations)
df_distance = pd.DataFrame(distance_matrix, columns=[f"Location_{i}" for i in range(num_locations)],
                           index=[f"Location_{i}" for i in range(num_locations)])
df_customer_demands = generate_customer_demands(num_customers)
df_truck_capacities = generate_truck_capacities(num_trucks)

# Save data to CSVs
df_distance.to_csv("distance_matrix.csv", index=True)
df_customer_demands.to_csv("customer_demands.csv", index=False)
df_truck_capacities.to_csv("truck_capacities.csv", index=False)

# ====================
# Integration Testing
# ====================
truck_capacity = df_truck_capacities["Capacity"][0]
routes_nn = nearest_neighbor_vrp(distance_matrix, df_customer_demands["Demand"].tolist(), truck_capacity)
print("Routes (Nearest Neighbor):", routes_nn)

# Visualization
locations = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_locations)]
visualize_routes(routes_nn, locations)
