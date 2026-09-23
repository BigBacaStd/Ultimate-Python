#Python script

import matplotlib.pyplot as plt
"""
A number raised to the third power is a cube. Plot the first five
cubic numbers  and then plot the first 5,000 cubic numbers. 
"""
input_values = range(1, 1001)
cubes = [x**3 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Blues, s=10)

# Set chat title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.show()