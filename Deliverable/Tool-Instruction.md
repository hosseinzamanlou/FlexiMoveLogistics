# Tool Instruction: Concise, Unified, and Effective

## Tool Description
The **FlexiMove Route Optimization AI Agent** is a modular and scalable solution designed to streamline logistics operations. It calculates optimal delivery routes, predicts customer demand, and dynamically adjusts routes based on real-time traffic, weather, and new order updates. Built with a focus on efficiency and sustainability, this tool leverages advanced algorithms to reduce operational costs while improving delivery times.

## Tool Functionality Guideline with Examples

### Core Functionality 1: Route Optimization
- **Scenario**:  
  If you want to calculate the most efficient routes for multiple delivery trucks while considering capacity constraints and minimizing travel distance.
- **Parameters**:
  - `distance_matrix`: A 2D matrix representing the distances between all locations.
  - `truck_capacity`: The maximum load a truck can carry in units.
  - `customer_demands`: A list of demands for each customer.
- **Example**:
  - **Input**:
    ```json
    {
        "distance_matrix": [[0, 12, 15, 20], [12, 0, 10, 25], [15, 10, 0, 30], [20, 25, 30, 0]],
        "truck_capacity": 10,
        "customer_demands": [0, 3, 5, 2]
    }
    ```
  - **Output**:
    ```json
    {
        "optimized_routes": [["Depot", "Customer_1", "Customer_3", "Depot"], ["Depot", "Customer_2", "Depot"]],
        "total_distance": 45
    }
    ```

### Core Functionality 2: Demand Forecasting
- **Scenario**:  
  If you want to predict upcoming delivery demand to allocate resources efficiently during peak periods.
- **Parameters**:
  - `historical_demand_data`: Time-series data of previous customer demands.
  - `seasonality`: Specify whether weekly or monthly trends should be considered.
- **Example**:
  - **Input**:
    ```json
    {
        "historical_demand_data": [100, 120, 130, 150, 140, 160],
        "seasonality": "monthly"
    }
    ```
  - **Output**:
    ```json
    {
        "predicted_demand": [170, 180, 190],
        "time_period": ["Month_7", "Month_8", "Month_9"]
    }
    ```

### Core Functionality 3: Real-Time Adjustment
- **Scenario**:  
  If you want to adjust routes dynamically due to traffic, weather, or new order updates.
- **Parameters**:
  - `live_traffic_data`: Real-time traffic information affecting travel times.
  - `weather_conditions`: Weather impacts that may delay deliveries.
  - `new_orders`: Newly received customer orders.
- **Example**:
  - **Input**:
    ```json
    {
        "live_traffic_data": [[0, 10, 15, 30], [10, 0, 20, 25], [15, 20, 0, 40], [30, 25, 40, 0]],
        "weather_conditions": [0, 2, 3, 1],
        "new_orders": [{"CustomerID": "Customer_4", "Demand": 4}]
    }
    ```
  - **Output**:
    ```json
    {
        "updated_routes": [["Depot", "Customer_1", "Customer_3", "Depot"], ["Depot", "Customer_2", "Customer_4", "Depot"]],
        "adjusted_distance": 50
    }
    ```
![image](https://github.com/user-attachments/assets/7fb9327e-548d-4565-90d1-a2185fb8d674)

![image](https://github.com/user-attachments/assets/abc91594-050e-4bc3-a19e-af38274b9dc6)

![image](https://github.com/user-attachments/assets/c721f744-b816-474b-bab5-1f90e0a7e47c)


# FlexiMove Logistics Optimization Project

## Python Codebase

This markdown file contains all the Python scripts used in the FlexiMove Logistics Optimization project, including AI agent functions, data creation, route optimization, and visualizations.

---

### **1. Data Creation**

```python
import random
import pandas as pd
import numpy as np

# ====================
# 1. Distance Matrix
# ====================
def generate_distance_matrix(num_locations):
    distance_matrix = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(i + 1, num_locations):
            distance = random.randint(1, 50)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    
    data = []
    for i in range(num_locations):
        for j in range(num_locations):
            if i != j:
                data.append({"From": f"Location_{i}", "To": f"Location_{j}", "Distance": distance_matrix[i][j]})
    
    return pd.DataFrame(data), distance_matrix

# ====================
# 2. Customer Demands
# ====================
def generate_customer_demands(num_customers, max_demand=10):
    data = [{"CustomerID": f"Customer_{i}", "Demand": random.randint(1, max_demand)} for i in range(1, num_customers + 1)]
    data.insert(0, {"CustomerID": "Depot", "Demand": 0})
    return pd.DataFrame(data)

# ====================
# 3. Truck Capacities
# ====================
def generate_truck_capacities(num_trucks, max_capacity=15):
    data = [{"TruckID": f"Truck_{i}", "Capacity": random.randint(max_capacity - 5, max_capacity)} for i in range(1, num_trucks + 1)]
    return pd.DataFrame(data)

# ====================
# Generate Data
# ====================
num_locations = 10
num_customers = 9
num_trucks = 3

df_distance_matrix, raw_distance_matrix = generate_distance_matrix(num_locations)
df_customer_demands = generate_customer_demands(num_customers)
df_truck_capacities = generate_truck_capacities(num_trucks)

df_distance_matrix.to_csv("distance_matrix.csv", index=False)
df_customer_demands.to_csv("customer_demands.csv", index=False)
df_truck_capacities.to_csv("truck_capacities.csv", index=False)




from itertools import permutations
import math

# ====================
# Nearest Neighbor Heuristic
# ====================
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

# ====================
# Sweep Algorithm
# ====================
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


import matplotlib.pyplot as plt
import seaborn as sns

# ====================
# Visualize Routes
# ====================
def visualize_routes(locations, routes):
    plt.figure(figsize=(8, 8))
    depot = locations[0]
    customers = locations[1:]

    plt.scatter(depot[0], depot[1], c="red", s=150, label="Depot")
    plt.scatter(*zip(*customers), c="blue", s=100, label="Customers")
    for i, (x, y) in enumerate(customers, start=1):
        plt.text(x + 1, y + 1, f"C{i}", fontsize=9)

    for route in routes:
        route_coords = [locations[0]] + [locations[int(customer.split("_")[1])] for customer in route[1:-1]] + [locations[0]]
        x, y = zip(*route_coords)
        plt.plot(x, y, marker="o", label=f"Route: {' → '.join(route)}")

    plt.title("Optimized Delivery Routes")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.show()

# ====================
# Visualize Demand Forecasting
# ====================
def visualize_forecasting(df_forecasting):
    plt.figure(figsize=(10, 6))
    plt.plot(df_forecasting["Months"], df_forecasting["Demand"], marker="o", label="Actual Demand")
    plt.plot(df_forecasting["Months"], df_forecasting["Forecast"], marker="x", linestyle="--", label="Forecasted Demand")
    plt.title("Demand Forecasting")
    plt.xlabel("Months")
    plt.ylabel("Demand")
    plt.legend()
    plt.grid()
    plt.show()


# Example Usage for Nearest Neighbor
routes = nearest_neighbor_vrp(raw_distance_matrix, [0, 3, 5, 2, 4, 6, 2, 3, 4, 3], 10)
print("Routes:", routes)

# Example Usage for Visualization
locations = [(0, 0), (1, 3), (4, 4), (5, 1), (2, 5), (3, 2), (5, 5), (6, 1), (3, 4), (7, 6)]
visualize_routes(locations, [["Depot", "Customer_1", "Customer_3", "Depot"], ["Depot", "Customer_2", "Depot"]])

