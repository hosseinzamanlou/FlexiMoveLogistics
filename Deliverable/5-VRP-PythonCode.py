import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

# ====================
# Data Generation
# ====================
def generate_coordinates(num_locations):
    """Generate random coordinates for locations."""
    return [(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_locations)]

def generate_distance_matrix(coordinates):
    """Generate a symmetric distance matrix for locations based on coordinates."""
    num_locations = len(coordinates)
    distance_matrix = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(i + 1, num_locations):
            distance = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

# ====================
# Algorithms
# ====================
# Nearest Neighbor Heuristic
def nearest_neighbor_vrp(distance_matrix, num_trucks=1):
    n_customers = len(distance_matrix)
    visited = [False] * n_customers
    visited[0] = True
    routes = [[] for _ in range(num_trucks)]
    truck_index = 0

    while not all(visited):
        current_location = routes[truck_index][-1] if routes[truck_index] else 0
        nearest_customer = None
        shortest_distance = float('inf')

        for i in range(1, n_customers):
            if not visited[i] and distance_matrix[current_location][i] < shortest_distance:
                shortest_distance = distance_matrix[current_location][i]
                nearest_customer = i

        if nearest_customer is not None:
            routes[truck_index].append(nearest_customer)
            visited[nearest_customer] = True
        truck_index = (truck_index + 1) % num_trucks

    # Ensure all routes start and end at the depot
    for route in routes:
        route.insert(0, 0)  # Start from depot
        route.append(0)  # Return to depot
    return routes

# Sweep Algorithm
def calculate_polar_coordinates(coordinates):
    """Convert Cartesian coordinates to polar coordinates for Sweep Algorithm."""
    depot = coordinates[0]
    polar_coordinates = []
    for i, (x, y) in enumerate(coordinates):
        angle = math.atan2(y - depot[1], x - depot[0]) * (180 / math.pi)
        angle = angle if angle >= 0 else 360 + angle
        polar_coordinates.append((i, angle))
    return sorted(polar_coordinates, key=lambda x: x[1])

def sweep_algorithm(polar_coordinates, num_trucks=1):
    """Cluster customers using the Sweep Algorithm."""
    clusters = [[] for _ in range(num_trucks)]
    cluster_index = 0

    for i, (customer_id, _) in enumerate(polar_coordinates):
        if customer_id != 0:
            clusters[cluster_index].append(customer_id)
            cluster_index = (cluster_index + 1) % num_trucks

    # Ensure all clusters start and end at the depot
    for cluster in clusters:
        cluster.insert(0, 0)  # Start from depot
        cluster.append(0)  # Return to depot
    return clusters

# 2-Opt Algorithm
def calculate_total_distance(route, distance_matrix):
    """Calculate the total distance of a route."""
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

def two_opt(routes, distance_matrix):
    """Optimize a set of routes using 2-Opt."""
    optimized_routes = []
    for route in routes:
        best_route = route
        best_distance = calculate_total_distance(route, distance_matrix)
        improved = True

        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route) - 1):
                    new_route = route[:i] + route[i:j + 1][::-1] + route[j + 1:]
                    new_distance = calculate_total_distance(new_route, distance_matrix)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_route = new_route
                        improved = True
        optimized_routes.append(best_route)
    return optimized_routes

# ====================
# Visualization Functions
# ====================
def visualize_static(coordinates, title, routes_one, routes_two):
    fig, axs = plt.subplots(1, 2, figsize=(18, 8))
    colors = sns.color_palette("hsv", len(coordinates))
    route_colors = sns.color_palette("Set2", len(routes_two))  # Colors for two vehicle routes

    # Plot for one vehicle
    axs[0].set_title(f"{title} (1 Vehicle)")
    for route in routes_one:
        for i in range(len(route) - 1):
            start, end = route[i], route[i + 1]
            axs[0].arrow(coordinates[start][0], coordinates[start][1], 
                         coordinates[end][0] - coordinates[start][0], 
                         coordinates[end][1] - coordinates[start][1], 
                         head_width=0.3, length_includes_head=True, color='black')
    for i, (x, y) in enumerate(coordinates):
        label = "Depot" if i == 0 else f"Customer_{i}"
        axs[0].scatter(x, y, c=[colors[i]], s=100)
        axs[0].text(x + 0.3, y + 0.3, label, fontsize=9)

    # Plot for two vehicles
    axs[1].set_title(f"{title} (2 Vehicles)")
    for idx, route in enumerate(routes_two):
        route_color = route_colors[idx]  # Use a different color for each route
        for i in range(len(route) - 1):
            start, end = route[i], route[i + 1]
            axs[1].arrow(coordinates[start][0], coordinates[start][1], 
                         coordinates[end][0] - coordinates[start][0], 
                         coordinates[end][1] - coordinates[start][1], 
                         head_width=0.3, length_includes_head=True, color=route_color)
    for i, (x, y) in enumerate(coordinates):
        label = "Depot" if i == 0 else f"Customer_{i}"
        axs[1].scatter(x, y, c=[colors[i]], s=100)
        axs[1].text(x + 0.3, y + 0.3, label, fontsize=9)

    for ax in axs:
        ax.set_xlabel("X Coordinate")
        ax.set_ylabel("Y Coordinate")
        ax.grid()
    
    plt.tight_layout()
    plt.show()

# ====================
# Main Execution
# ====================
def visualize_all_addresses(coordinates):
    """Visualize all addresses on a 2D plane with distinct colors."""
    plt.figure(figsize=(8, 8))
    colors = sns.color_palette("hsv", len(coordinates))

    # Plot each address with a unique color
    for i, (x, y) in enumerate(coordinates):
        label = "Depot" if i == 0 else f"Customer_{i}"
        plt.scatter(x, y, c=[colors[i]], s=150, label=label)
        plt.text(x + 0.3, y + 0.3, label, fontsize=9)

    plt.title("All Addresses on 2D Plane")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid()
    plt.legend()
    plt.show()

# ====================
# Revised Example Usage
# ====================

# Step 1: Generate coordinates and distance matrix
num_locations = 10
coordinates = generate_coordinates(num_locations)
distance_matrix = generate_distance_matrix(coordinates)

# Step 2: Visualize all addresses
visualize_all_addresses(coordinates)

# Step 3: Execute Route Optimization Algorithms and Visualize
# Nearest Neighbor Heuristic
nn_route_1 = nearest_neighbor_vrp(distance_matrix, num_trucks=1)
nn_route_2 = nearest_neighbor_vrp(distance_matrix, num_trucks=2)
visualize_static(coordinates, "Nearest Neighbor Heuristic", nn_route_1, nn_route_2)

# Sweep Algorithm
polar_coords = calculate_polar_coordinates(coordinates)
sweep_route_1 = sweep_algorithm(polar_coords, num_trucks=1)
sweep_route_2 = sweep_algorithm(polar_coords, num_trucks=2)
visualize_static(coordinates, "Sweep Algorithm", sweep_route_1, sweep_route_2)

# 2-Opt Algorithm (starting from Nearest Neighbor route)
opt_route_1 = two_opt(nn_route_1, distance_matrix)
opt_route_2 = two_opt(nn_route_2, distance_matrix)
visualize_static(coordinates, "2-Opt Algorithm", opt_route_1, opt_route_2)
