
import matplotlib.pyplot as plt

# Sample data for x and y coordinates
x1 = [10000, 20000, 40000, 80000, 160000 ]
y1 = [0.039667, 0.15267, 0.606333, 2.430333, 9.72833]
x2 = [10000000, 20000000, 40000000, 80000000, 160000000]
y2 = [0.017333, 0.03533, 0.081333, 0.154333, 0.289333]
# Plotting the scatter plot
plt.scatter(x1, y1, color='blue', marker='o', label='Algorithm 1')
plt.scatter(x2, y2, color='red', marker='x', label='Algorithm 2')

# Adding labels and title
plt.xlabel('Input Size (n)')
plt.ylabel('Average Execution Time (ms)')
plt.title('Time plot of Algorithms in C Code')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()