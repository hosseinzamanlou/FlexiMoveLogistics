# FlexiMove Logistics Optimization

Welcome to the **FlexiMove Logistics Optimization** project! This repository documents our journey in solving complex vehicle routing problems (VRP) using AI-driven algorithms, innovative data visualization, and a step-by-step exploration of real-world logistics challenges.

---

## 🚀 **Project Overview**
FlexiMove Logistics aims to address the challenges of modern logistics by developing an intelligent, adaptable AI agent to optimize delivery routes. The project focuses on achieving cost efficiency, reducing environmental impact, and ensuring timely deliveries, thereby enhancing overall customer satisfaction.

Our AI agent integrates multiple routing optimization algorithms and is designed to:
- Minimize travel distances for all deliveries.
- Dynamically adapt to real-time conditions such as traffic or new customer orders.
- Provide a user-friendly interface with informative data visualizations to understand optimization improvements.

---

## 🛠️ **Solution Overview**
Our solution utilizes heuristic and clustering-based algorithms combined with real-time adjustment capabilities to tackle the VRP problem effectively. The implemented approaches include:

### **1. Nearest Neighbor Heuristic**
This heuristic provides an efficient way to generate initial routes by prioritizing the nearest unvisited customers. It aims to quickly identify a reasonable solution that can be further refined.

### **2. Sweep Algorithm**
The Sweep Algorithm clusters customers based on their angular positions relative to the depot, forming smaller, more manageable groups that allow for optimal routing. Each cluster then undergoes further optimization, resembling a Traveling Salesman Problem (TSP) solution.

### **3. 2-Opt Algorithm**
The initial routes are further refined using the 2-Opt algorithm. This iterative algorithm looks for opportunities to swap two segments within a route to achieve a lower total distance, improving overall efficiency.



Key functionalities include:
- **Static and Dynamic Route Optimization**: Efficiently calculate routes for different vehicle configurations.
- **Visual Comparison of One vs. Two Vehicles**: Compare route efficiency using one or two vehicles to help demonstrate the impact of increased fleet capacity.
- **Performance Tracking**: Evaluation metrics like distance traveled, on-time delivery rates, and overall efficiency improvements are generated.

---

## 📊 **Datasets**
Three synthetic datasets form the backbone of our logistics optimization solution:

1. **Distance Matrix**: Represents pairwise distances between depot and customer locations, generated programmatically based on geographic coordinates.
2. **Customer Demands**: Provides customer demand values at each location, designed to represent realistic logistics demands.
3. **Truck Capacities**: Maximum load capacities for each vehicle in the fleet, used to ensure efficient load balancing across deliveries.

All datasets are automatically generated and formatted for scalability, allowing for easy modifications.

---

## 🧠 **Core Algorithms Explained**

### **1. Nearest Neighbor Heuristic**
Generates initial routes by always selecting the nearest unvisited customer, resulting in a quick and relatively optimized solution. This heuristic is especially useful when a fast response is required.

### **2. Sweep Algorithm**
Clusters customers based on their geographic position, allowing for efficient group deliveries. The clustering is then optimized using TSP heuristics to minimize travel within each group.

### **3. 2-Opt Algorithm**
Further optimizes initial routes by systematically reversing segments to find a route with reduced distance. This ensures the final route achieves significant efficiency gains over the initial heuristic.

---

## 📈 **Performance Metrics**
To evaluate the solution's performance, we use the following key metrics:

- **On-Time Delivery Rate**: Percentage of deliveries completed within the expected time frame.
  
  \((	ext{Deliveries Made on Time} / 	ext{Total Deliveries}) 	imes 100\%\)

- **Total Distance Traveled**: The sum of all distances covered by all vehicles. A lower value indicates better optimization.

- **Fuel Efficiency Improvement**: Measures the percentage improvement in fuel consumption compared to a baseline scenario.
  
  \((	ext{Baseline Fuel} - 	ext{Optimized Fuel}) / 	ext{Baseline Fuel} 	imes 100\%\)

- **Customer Satisfaction**: Calculated based on post-delivery feedback, reflecting the efficiency and timeliness of deliveries.

---

## 🖥️ **How to Run**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/hosseinzamanlou/FlexiMoveLogistics.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Synthetic Datasets**:
   ```bash
   python generate_datasets.py
   ```

4. **Run Route Optimization Solutions**:
   ```bash
   python run_vrp_solutions.py
   ```

5. **Visualize Routes and Metrics**:
   - Open the generated results in your browser or review the plots saved in the `outputs/` folder.

---

## 📊 **Visualization Examples**
The solution provides visual representations of:

1. **All Addresses**: Displays all customer locations and depot on a 2D plane using distinct colors.
2. **Static Route Optimization**: Shows results of the three route optimization algorithms (Nearest Neighbor, Sweep, 2-Opt) for one-vehicle and two-vehicle scenarios.
3. **Comparative Analysis**: Visual matrices highlight the difference between using a single vehicle vs. multiple vehicles, demonstrating the efficiency improvements.




![All Addresses on 2D Plane](https://github.com/user-attachments/assets/53afb5ae-e127-4c64-856d-e493db71cc1d)

![Nearest Neighbor Routes Comparison](https://github.com/user-attachments/assets/929eb399-8ce1-43cf-8ecf-44b8f80073f5)



![Sweep Algorithm Routes Comparison](https://github.com/user-attachments/assets/513e4c8a-5bc0-4364-9003-1a375fc91044)



![2-Opt Optimized Routes Comparison](https://github.com/user-attachments/assets/a8211c16-6e73-44b3-a32a-134b32c112f5)


---

## 🤝 **Contributors**
- **​Alexander Gafirov | Cédric Fink | Hossein Zamanlou | Patricia Abel | Patrick Sigg **: Original concept, data generation, algorithm implementation, and optimization.

We welcome feedback, suggestions, and collaborations! Please feel free to open an issue or submit a pull request if you'd like to contribute.

---

## 📜 **License**
This project is licensed under the MIT License.

Happy optimizing! 🚛

---

