# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load data from Excel file
file_path = "dos_trial.xlsx"  # Change this to your actual file
sheet_name = "Sheet1"  # Change if needed
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Assume first column is energy, rest are projected DOS
energy = df.iloc[:, 0]
columns = df.columns[1:]
num_planes = len(columns)

# Define colors
colors = plt.cm.plasma(np.linspace(0.1, 0.9, num_planes))

# Create figure and 3D axis with enhanced aesthetics
fig = plt.figure(figsize=(12, 8), dpi=300)
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)  # Remove grid for a cleaner look

# Plot each PDOS in a separate vertical plane with transparency
for i, (col, color) in enumerate(zip(columns, colors)):
    pdos = df[col]
    x = np.full_like(energy, i)  # Position in the 3D space
    ax.plot(x, energy, pdos, color=color, linewidth=0.75, zorder=2)

    # Create filled region using Poly3DCollection with smooth shading
    verts = [list(zip(x, energy, pdos))]
    poly = Poly3DCollection(verts, color=color, alpha=0.6, edgecolor='k', linewidths=0.5)
    ax.add_collection3d(poly)

# Plot the total DOS at the back with bold lines
total_dos = df.iloc[:, 1:].sum(axis=1)
x_total = np.full_like(energy, -1)
ax.plot(x_total, energy, total_dos, color='black', linewidth=0.5, zorder=3)

# Create filled region for total DOS
verts_total = [list(zip(x_total, energy, total_dos))]
poly_total = Poly3DCollection(verts_total, color='gray', alpha=0.7, edgecolor='k', linewidths=0.5)
ax.add_collection3d(poly_total)

# Labels and aesthetics
ax.set_xlabel("", fontsize=14, fontweight='bold')  # Remove x-axis label
ax.set_ylabel("Energy (eV)", fontsize=14, fontweight='bold', labelpad=15)
ax.set_zlabel("Density of States", fontsize=14, fontweight='bold', labelpad=15)

# Remove tick marks and labels on the x-axis (width axis)
ax.set_xticks([])  # Remove tick marks
ax.set_xticklabels([])  # Remove tick labels

# Set x-limits for a boxed effect and adjust the axis ranges
ax.set_xlim(-1, num_planes)
ax.set_ylim(energy.min(), energy.max())  # Ensure y-limits correspond to the energy range
ax.set_zlim(0, max(total_dos))  # Adjust z-limits to match the range of the total DOS

ax.view_init(elev=25, azim=-50)  # Adjust for better visibility

# Add tick marks with labels at points where each graph is drawn
for i, col in enumerate(columns):
    ax.text(i, energy.min() - 0.1 * (energy.max() - energy.min()), 0, col,
            fontsize=12, rotation=90, verticalalignment='bottom', horizontalalignment='center', fontweight='bold')

# Set box around the figure by modifying pane edgecolors and faces
ax.xaxis.pane.set_edgecolor('black')  # Add black edge for the x-axis pane
ax.yaxis.pane.set_edgecolor('black')  # Add black edge for the y-axis pane
ax.zaxis.pane.set_edgecolor('black')  # Add black edge for the z-axis pane
ax.xaxis.pane.set_facecolor('white')  # Set background to white
ax.yaxis.pane.set_facecolor('white')
ax.zaxis.pane.set_facecolor('white')


# Add box lines manually to ensure the box is drawn around the figure
# Define box corners
x_limits = [-1, num_planes]
y_limits = [energy.min(), energy.max()]
z_limits = [0,  max(total_dos)]  # Add margin for better visualization

# Manually draw the 3D bounding box using ax.plot
box_edges = [
    [[x_limits[0], x_limits[1]], [y_limits[0], y_limits[0]], [z_limits[0], z_limits[0]]],  # Bottom front
    [[x_limits[0], x_limits[1]], [y_limits[1], y_limits[1]], [z_limits[0], z_limits[0]]],  # Bottom back
    [[x_limits[0], x_limits[1]], [y_limits[0], y_limits[0]], [z_limits[1], z_limits[1]]],  # Top front
    [[x_limits[0], x_limits[1]], [y_limits[1], y_limits[1]], [z_limits[1], z_limits[1]]],  # Top back

    [[x_limits[0], x_limits[0]], [y_limits[0], y_limits[1]], [z_limits[0], z_limits[0]]],  # Left bottom
    [[x_limits[1], x_limits[1]], [y_limits[0], y_limits[1]], [z_limits[0], z_limits[0]]],  # Right bottom
    [[x_limits[0], x_limits[0]], [y_limits[0], y_limits[1]], [z_limits[1], z_limits[1]]],  # Left top
    [[x_limits[1], x_limits[1]], [y_limits[0], y_limits[1]], [z_limits[1], z_limits[1]]],  # Right top

    [[x_limits[0], x_limits[0]], [y_limits[0], y_limits[0]], [z_limits[0], z_limits[1]]],  # Front left
    [[x_limits[1], x_limits[1]], [y_limits[0], y_limits[0]], [z_limits[0], z_limits[1]]],  # Front right
    [[x_limits[0], x_limits[0]], [y_limits[1], y_limits[1]], [z_limits[0], z_limits[1]]],  # Back left
    [[x_limits[1], x_limits[1]], [y_limits[1], y_limits[1]], [z_limits[0], z_limits[1]]],  # Back right
]

# Plot the edges of the bounding box
for edge in box_edges:
    ax.plot(edge[0], edge[1], edge[2], color='black', linewidth=1.2)
for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
    axis.set_tick_params(width=2, colors='black')

plt.title("Atom-Projected Density of States", fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

