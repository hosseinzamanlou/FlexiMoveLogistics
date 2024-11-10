import pandas as pd

# Creating synthetic datasets based on the user's specifications

# 1. Historical Delivery Data
historical_delivery_data = pd.DataFrame({
    "route_id": ["R001", "R002", "R003", "R004", "R005"],
    "start_location": ["46.94809,7.44744"] * 5,
    "end_location": ["46.9478,7.4490", "46.9490,7.4502", "46.9488,7.4532", "46.9485,7.4469", "46.94809,7.44744"],
    "intermediate_stops": ["46.94797,7.44461;46.9475,7.4512", "46.9483,7.4514;46.9490,7.4502", "46.9488,7.4532;46.9486,7.4491",
                           "46.9485,7.4469;46.9490,7.4481", "46.9478,7.4490;46.9482,7.4500"],
    "route_distance_km": [12.5, 8.3, 10.1, 11.0, 9.5],
    "estimated_duration_hr": [0.45, 0.3, 0.4, 0.42, 0.35],
    "actual_duration_hr": [0.5, 0.35, 0.4, 0.47, 0.36],
    "day_of_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "time_of_day": ["morning", "afternoon", "morning", "afternoon", "morning"],
    "delivery_window_start": ["08:00", "13:00", "09:00", "14:00", "07:00"],
    "delivery_window_end": ["10:00", "15:00", "11:00", "16:00", "09:00"]
})

# 2. Vehicle and Fleet Data
vehicle_fleet_data = pd.DataFrame({
    "vehicle_id": ["V001", "V002", "V003", "V004", "V005"],
    "vehicle_type": ["small", "medium", "large", "electric", "small"],
    "capacity": [1000, 2000, 4000, 1200, 1000],
    "fuel_efficiency": [10.5, 8.0, 6.5, 0.0, 10.0],
    "current_location": ["46.94809,7.44744", "46.94797,7.44461", "46.9483,7.4514", "46.9488,7.4532", "46.9485,7.4469"],
    "maintenance_status": ["in-service", "maintenance_required", "in-service", "in-service", "in-service"],
    "available_hours": ["08:00-18:00"] * 5
})

# 3. Traffic and Environmental Data
traffic_weather_data = pd.DataFrame({
    "route_id": ["R001", "R002", "R003", "R004", "R005"],
    "traffic_condition": ["heavy", "moderate", "light", "heavy", "moderate"],
    "time_of_day": ["morning", "afternoon", "morning", "afternoon", "morning"],
    "weather_condition": ["rain", "clear", "snow", "clear", "rain"],
    "traffic_delay_min": [15, 8, 5, 20, 10],
    "weather_delay_min": [5, 0, 10, 0, 7]
})

# 4. Customer and Demand Data
customer_demand_data = pd.DataFrame({
    "customer_id": ["C001", "C002", "C003", "C004", "C005"],
    "customer_priority": ["high", "medium", "high", "low", "medium"],
    "order_frequency": ["daily", "weekly", "daily", "monthly", "daily"],
    "expected_volume": [5, 15, 10, 20, 7],
    "service_level_agreement": ["2 hours", "3 hours", "1 hour", "4 hours", "2 hours"],
    "location": ["46.94797,7.44461", "46.9483,7.4514", "46.9488,7.4532", "46.9485,7.4469", "46.94809,7.44744"],
    "preferred_delivery_times": ["08:00-10:00", "13:00-15:00", "07:00-09:00", "14:00-16:00", "09:00-11:00"]
})

# 5. Real-Time Order Data
real_time_orders = pd.DataFrame({
    "order_id": ["O001", "O002", "O003", "O004", "O005"],
    "customer_id": ["C001", "C002", "C003", "C004", "C005"],
    "pickup_location": ["46.94797,7.44461", "46.9483,7.4514", "46.9488,7.4532", "46.9485,7.4469", "46.94809,7.44744"],
    "delivery_location": ["46.94809,7.44744", "46.9488,7.4532", "46.94797,7.44461", "46.94809,7.44744", "46.9483,7.4514"],
    "pickup_time": ["08:30", "13:15", "07:30", "14:30", "09:00"],
    "delivery_deadline": ["10:00", "15:00", "09:00", "16:00", "11:00"],
    "status": ["pending", "in-transit", "completed", "pending", "in-transit"]
})

# 6. Cost and Efficiency Data
cost_efficiency_data = pd.DataFrame({
    "route_id": ["R001", "R002", "R003", "R004", "R005"],
    "fuel_cost": [20.0, 15.0, 18.0, 22.0, 16.0],
    "driver_cost": [30.0, 25.0, 27.0, 32.0, 28.0],
    "penalties": [5.0, 0.0, 7.0, 0.0, 3.0],
    "total_cost": [55.0, 40.0, 52.0, 54.0, 47.0]
})

# 7. Performance Metrics Data
performance_metrics = pd.DataFrame({
    "route_id": ["R001", "R002", "R003", "R004", "R005"],
    "on_time_delivery": [1, 1, 0, 1, 1],
    "customer_feedback": [4, 5, 3, 4, 4],
    "average_delay": [5, 3, 10, 2, 4],
    "fuel_consumed": [15.0, 12.0, 14.0, 16.0, 13.0],
    "actual_cost": [55.0, 40.0, 52.0, 54.0, 47.0]
})

# Save all DataFrames as .csv files
historical_delivery_data.to_csv("c:/Users/hosse/FlexiMove/historical_delivery_data.csv", index=False)
vehicle_fleet_data.to_csv("c:/Users/hosse/FlexiMove/vehicle_fleet_data.csv", index=False)
traffic_weather_data.to_csv("c:/Users/hosse/FlexiMove/traffic_weather_data.csv", index=False)
customer_demand_data.to_csv("c:/Users/hosse/FlexiMove/customer_demand_data.csv", index=False)
real_time_orders.to_csv("c:/Users/hosse/FlexiMove/real_time_orders.csv", index=False)
cost_efficiency_data.to_csv("c:/Users/hosse/FlexiMove/cost_efficiency_data.csv", index=False)
performance_metrics.to_csv("c:/Users/hosse/FlexiMove/performance_metrics.csv", index=False)
