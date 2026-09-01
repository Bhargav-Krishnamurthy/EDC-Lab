import matplotlib.pyplot as plt

# Data extracted from image_b7c9a8.png
x = [
    0.7, 0.8, 0.9, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 
    1.42, 1.44, 1.46, 1.48, 1.5, 1.52, 1.54, 1.56, 1.58, 1.6, 1.62, 
    1.64, 1.66, 1.68, 1.7, 1.72, 1.74, 1.76, 1.78, 1.8, 1.9, 2
]

y = [
    9.9936, 9.9935, 9.9934, 9.9928, 9.992, 9.9901, 9.987, 9.9808, 
    9.968, 9.945, 9.9, 9.811, 9.7565, 9.6845, 9.591, 9.47, 9.314, 
    9.113, 8.856, 8.52, 8.12, 7.6, 6.96, 6.17, 5.21, 4.04, 2.62, 
    1.08, 0.814, 0.758, 0.728, 0.708, 0.67, 0.67
]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='.', linestyle='-', color='b')

# Add labels, title, and grid
plt.title('Voltage Transfer Characteristic (Extracted Data)')
plt.xlabel('Input (e.g., $V_{in}$)')
plt.ylabel('Output (e.g., $V_{out}$)')
plt.grid(True)

# Display the graph
plt.savefig("PartA_graph.png")