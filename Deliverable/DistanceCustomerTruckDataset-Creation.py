import random
import pandas as pd
import numpy as np

# ====================
# 1. Distance Matrix
# ====================
def generate_distance_matrix(num_locations):
    # Generate random distances between locations
    distance_matrix = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(i + 1, num_locations):
            distance = random.randint(1, 50)  # Random distance between 1 and 50
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance  # Symmetric matrix
    
    # Convert to DataFrame
    data = []
    for i in range(num_locations):
        for j in range(num_locations):
            if i != j:
                data.append({"From": f"Location_{i}", "To": f"Location_{j}", "Distance": distance_matrix[i][j]})
    
    df_distance = pd.DataFrame(data)
    return df_distance

# ====================
# 2. Customer Demands
# ====================
def generate_customer_demands(num_customers, max_demand=10):
    # Generate random demands for each customer
    data = [{"CustomerID": f"Customer_{i}", "Demand": random.randint(1, max_demand)} for i in range(1, num_customers + 1)]
    # Add depot with zero demand
    data.insert(0, {"CustomerID": "Depot", "Demand": 0})
    df_demands = pd.DataFrame(data)
    return df_demands

# ====================
# 3. Truck Capacity
# ====================
def generate_truck_capacities(num_trucks, max_capacity=15):
    # Generate random capacities for each truck
    data = [{"TruckID": f"Truck_{i}", "Capacity": random.randint(max_capacity - 5, max_capacity)} for i in range(1, num_trucks + 1)]
    df_capacity = pd.DataFrame(data)
    return df_capacity

# ====================
# Generate Data
# ====================
num_locations = 15  # Including depot
num_customers = 15   # Excluding depot
num_trucks = 4

# Generate datasets
df_distance_matrix = generate_distance_matrix(num_locations)
df_customer_demands = generate_customer_demands(num_customers)
df_truck_capacities = generate_truck_capacities(num_trucks)

# Save to CSV
df_distance_matrix.to_csv("distance_matrix.csv", index=False)
df_customer_demands.to_csv("customer_demands.csv", index=False)
df_truck_capacities.to_csv("truck_capacities.csv", index=False)

# ====================
# Summary and Display
# ====================
print("Synthetic Distance Matrix:")
print(df_distance_matrix.head())

print("\nSynthetic Customer Demands:")
print(df_customer_demands.head())

print("\nSynthetic Truck Capacities:")
print(df_truck_capacities.head())
