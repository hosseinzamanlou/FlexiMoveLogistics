# Tool Instruction: Comprehensive AI-Driven Logistics Optimization Tool

## Tool Description
The **FlexiMove Logistics Optimization AI Agent** is a scalable and modular solution tailored for dynamic logistics challenges. This tool integrates advanced route optimization algorithms, demand forecasting models, and real-time adjustments to provide actionable insights and solutions. Designed for sustainability and operational efficiency, it minimizes delivery costs and enhances customer satisfaction.

## Tool Functionality Guideline with Examples

### Core Functionality 1: Route Optimization
- **Scenario**:  
  Optimizing delivery routes across multiple trucks while adhering to capacity constraints and minimizing total distance traveled.
- **Parameters**:
  - `distance_matrix`: A 2D array representing distances between locations.
  - `truck_capacity`: Maximum load a truck can carry.
  - `customer_demands`: List of customer demands.
- **Algorithms**:
  - **Nearest Neighbor**: Creates initial routes based on proximity.
  - **Sweep Algorithm**: Groups customers into clusters by geographic proximity.
  - **2-Opt Refinement**: Refines routes to minimize total distance further.
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
  Predicting delivery demand for better resource allocation and efficient scheduling during peak periods.
- **Parameters**:
  - `historical_demand_data`: Time-series data of past customer demands.
  - `seasonality`: Indicate whether weekly or monthly trends are considered.
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
  Dynamically adjusting routes in response to real-time updates, such as traffic congestion, weather delays, or new customer orders.
- **Parameters**:
  - `live_traffic_data`: Current traffic data affecting travel times.
  - `weather_conditions`: Weather impacts for route adjustments.
  - `new_orders`: Details of newly received customer orders.
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

### Core Functionality 4: Visualization
- **Scenario**:  
  Visualizing delivery routes, demand forecasts, and algorithm performance for better understanding and presentation.
- **Visualization Outputs**:
  - **Delivery Routes**: Displays optimized routes between depot and customers.
  - **Demand Forecasting**: Shows demand trends and predictions.
  - **Real-Time Adjustments**: Highlights updated routes in response to live data.
- **Example Visualization**:
  - **Route Plot**: A visual graph displaying optimized delivery paths for trucks, with annotated customer locations and depot.
  - **Demand Trend**: A line chart comparing historical demands with predicted values.

### Key Features
- Modular architecture for easy customization and scalability.
- Comprehensive YAML configurations for seamless integration with AI platforms.
- Real-time adaptability to dynamic logistics conditions.

### Example AI Agent Deployment
- **Input Requirements**:
  - YAML configuration file specifying functionality, parameters, and interaction protocols.
  - Data sources (e.g., distance matrices, historical demands, live traffic updates).
- **Output Deliverables**:
  - Optimized routes with visualizations.
  - Forecasted demand trends.
  - Evaluation metrics for supply chain performance.

---

### How to Use
1. **Prepare Input Data**:
   - Ensure `distance_matrix.csv`, `customer_demands.csv`, and `truck_capacities.csv` are available.
   - For real-time data, integrate traffic and weather APIs.

2. **Run Algorithms**:
   - Execute Python scripts for route optimization and demand forecasting.
   - Visualize results using the provided plotting functions.

3. **Deploy AI Agent**:
   - Provide the YAML file to an AI platform.
   - Use APIs for real-time data integration and automation.

4. **Evaluate Metrics**:
   - Use calculated metrics like on-time delivery rate, total distance, and fuel efficiency for performance analysis.

---

Let me know if additional functionalities or explanations are needed!
