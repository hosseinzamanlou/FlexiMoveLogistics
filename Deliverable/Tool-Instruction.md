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
