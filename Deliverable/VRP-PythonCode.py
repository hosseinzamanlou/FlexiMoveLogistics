import random
import pandas as pd
import numpy as np

def generate_distance_matrix(num_locations):
    distance_matrix = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(i + 1, num_locations):
            distance = random.randint(1, 50)  # Random distance
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

def generate_customer_demands(num_customers, max_demand=10):
    demands = [{"CustomerID": f"Customer_{i}", "Demand": random.randint(1, max_demand)} for i in range(1, num_customers + 1)]
    demands.insert(0, {"CustomerID": "Depot", "Demand": 0})
    return pd.DataFrame(demands)

def generate_truck_capacities(num_trucks, max_capacity=15):
    capacities = [{"TruckID": f"Truck_{i}", "Capacity": random.randint(max_capacity - 5, max_capacity)} for i in range(1, num_trucks + 1)]
    return pd.DataFrame(capacities)

# Generate datasets
num_locations = 10
num_customers = 9
num_trucks = 3

distance_matrix = generate_distance_matrix(num_locations)
df_distance = pd.DataFrame(distance_matrix, columns=[f"Location_{i}" for i in range(num_locations)],
                           index=[f"Location_{i}" for i in range(num_locations)])
df_customer_demands = generate_customer_demands(num_customers)
df_truck_capacities = generate_truck_capacities(num_trucks)

# Save to CSV
df_distance.to_csv("distance_matrix.csv", index=True)
df_customer_demands.to_csv("customer_demands.csv", index=False)
df_truck_capacities.to_csv("truck_capacities.csv", index=False)


import pandas as pd
import numpy as np
from itertools import permutations
import math

# Load datasets
df_distance = pd.read_csv("distance_matrix.csv", index_col=0)
df_customer_demands = pd.read_csv("customer_demands.csv")
df_truck_capacities = pd.read_csv("truck_capacities.csv")

distance_matrix = df_distance.to_numpy()
customer_demands = df_customer_demands["Demand"].tolist()
truck_capacities = df_truck_capacities["Capacity"].tolist()

# Nearest Neighbor Heuristic
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

# Solve with Nearest Neighbor Heuristic
truck_capacity = truck_capacities[0]  # Example: Using first truck capacity
routes_nn = nearest_neighbor_vrp(distance_matrix, customer_demands, truck_capacity)
print("Routes (Nearest Neighbor):", routes_nn)





import matplotlib.pyplot as plt

# Example coordinates for visualization
coordinates = [(0, 0), (1, 3), (4, 4), (5, 1), (2, 5), (3, 2), (6, 3), (7, 1), (8, 5), (9, 3)]

def visualize_routes(routes, coordinates):
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

# Visualize Nearest Neighbor Routes
visualize_routes(routes_nn, coordinates)



import requests

def test_google_maps_api():
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": "New York, NY",
        "destinations": "Los Angeles, CA",
        "key": "YOUR_GOOGLE_MAPS_API_KEY"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Google Maps API Test Successful!")
    else:
        print("Google Maps API Test Failed:", response.text)

def test_weather_api():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "New York",
        "appid": "YOUR_WEATHER_API_KEY"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Weather API Test Successful!")
    else:
        print("Weather API Test Failed:", response.text)

# Run Tests
test_google_maps_api()
test_weather_api()



def test_integration():
    try:
        print("Testing data loading...")
        df_distance = pd.read_csv("distance_matrix.csv")
        df_customer_demands = pd.read_csv("customer_demands.csv")
        df_truck_capacities = pd.read_csv("truck_capacities.csv")
        print("Data loading successful!")

        print("Testing Nearest Neighbor Algorithm...")
        routes_nn = nearest_neighbor_vrp(distance_matrix, customer_demands, truck_capacity)
        print("Algorithm execution successful! Routes:", routes_nn)

        print("Testing Visualization...")
        visualize_routes(routes_nn, coordinates)
        print("Visualization successful!")
    except Exception as e:
        print("Integration Test Failed:", str(e))

# Run Integration Test
test_integration()




