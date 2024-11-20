# FlexiMove Logistics Optimization

Welcome to the **FlexiMove Logistics Optimization** project! This repository houses our journey toward solving real-world vehicle routing problems (VRP) using cutting-edge AI techniques and data-driven approaches.

---

## 🚀 **Project Overview**
In modern logistics, optimizing delivery routes is crucial for cost savings, sustainability, and on-time delivery. FlexiMove Logistics tackles this challenge by developing an AI-driven agent to:
- Minimize travel distances.
- Dynamically adapt to real-time changes like traffic or new orders.
- Ensure operational efficiency while maintaining customer satisfaction.

---

## 🛠️ **Solution Overview**
Our AI agent leverages heuristic and clustering algorithms, such as:
1. **Nearest Neighbor Heuristic**: Quickly generates initial routes.
2. **Sweep Algorithm with TSP Optimization**: Refines clusters into efficient delivery sequences.
3. **Dynamic Adjustments**: Adapts routes using live traffic, weather, and order data.

Key functionalities:
- **Route Optimization**: Finds the shortest, most efficient delivery paths.
- **Dynamic Adjustment**: Real-time updates for changing conditions.
- **Performance Evaluation**: Tracks metrics like on-time delivery rate, fuel efficiency, and customer satisfaction.

---

## 📊 **Datasets**
We use three synthetic datasets to power our solution:
1. **DistanceMatrix**: Pairwise distances between depot and customer locations.
2. **CustomerDemands**: Demand at each location.
3. **TruckCapacity**: Maximum load capacity of each vehicle.

All datasets are generated programmatically using Python and are structured for scalability.

---

## 🧠 **Core Algorithms**
### **1. Nearest Neighbor Heuristic**
A simple yet effective algorithm to generate initial routes by always visiting the nearest unvisited customer. 

### **2. Sweep Algorithm**
Groups customers into clusters based on angular positions and solves smaller TSP problems within each cluster.

### **3. Real-Time Adjustments**
Dynamically recalculates routes based on live inputs like traffic or new orders, ensuring minimal disruption.

---

## 📈 **Performance Metrics**
To evaluate the solution, we focus on:
- **On-Time Delivery Rate**: \((\text{Deliveries Made on Time} / \text{Total Deliveries}) \times 100\%\)
- **Total Distance Traveled**: Sum of all route distances.
- **Fuel Efficiency Improvement**: \((\text{Baseline Fuel} - \text{Optimized Fuel}) / \text{Baseline Fuel} \times 100\%\)
- **Customer Satisfaction**: Derived from post-delivery feedback.

---

## 🖥️ **How to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/hosseinzamanlou/FlexiMoveLogistics.git

### **Install dependencies:**
```bash
pip install -r requirements.txt


python generate_datasets.py


python run_vrp_solutions.py


Visualize Routes and Metrics:
Open the results in your browser or check the generated plots in the outputs/ folder.




