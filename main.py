import matplotlib.pyplot as plt

# Data for the X-axis (Technology nodes in nm) and Y (custom values)
x = [14, 28, 45, 90, 180]
y_vtcmos = [2.3, 2.5, 3, 6, 20]  # Custom values for the VTCMOS line
y_mtcmos = [y + 5 if x_val != 180 else y for x_val, y in zip(x, y_vtcmos)]  # Increase by 5, except at 180 nm

# Create the figure with a specified size
plt.figure(figsize=(10, 7))

# Set the labels for the axes
plt.xlabel("Technology nodes (nm)", fontsize=14)
plt.ylabel("Performance\nLeakage current in standby mode", fontsize=14)

# Set the title of the graph in bold
plt.title("Standby leakage current in MTCMOS and VTCMOS with technology scaling", fontsize=16, fontweight='bold')

# Plot the VTCMOS line with a thicker line and improved points
plt.plot(x, y_vtcmos, 'o-', label="VTCMOS", linewidth=2, markersize=8, color='blue', markerfacecolor='cyan', markeredgewidth=2)

# Add labels to the points with "nm" for VTCMOS
for i, txt in enumerate(x):
    plt.annotate(f'{txt} nm', (x[i], y_vtcmos[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12)

# Plot the MTCMOS line with a thicker line and improved points
plt.plot(x, y_mtcmos, 's--', color='orange', label="MTCMOS", linewidth=2, markersize=8, markerfacecolor='yellow', markeredgewidth=2)

# Add labels to the points with "nm" for MTCMOS, excluding the point at 180 nm
for i, txt in enumerate(x):
    if txt != 180:
        plt.annotate(f'{txt} nm', (x[i], y_mtcmos[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=12)

# Set limits for the axes to display only positive values
plt.xlim(0, max(x) + 10)
plt.ylim(0, max(y_mtcmos) + 5)

# Configure the axes display
plt.gca().spines['top'].set_visible(False)  # Hide the top spine
plt.gca().spines['right'].set_visible(False)  # Hide the right spine
plt.gca().spines['left'].set_position('zero')  # Position the left spine at zero
plt.gca().spines['bottom'].set_position('zero')  # Position the bottom spine at zero

# Remove the Y-axis tick labels
plt.gca().set_yticklabels([])

# Display the grid with dashed lines and partial transparency
plt.grid(True, linestyle='--', alpha=0.7)

# Display the legend with a specified font size
plt.legend(fontsize=12)

# Show the final graph
plt.show()