import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
#-------------------------------------------Functions; User input below-----------------------------------------------------------------------
def read_and_filter_pdos(file_path, energy_min, energy_max):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Ensure the first column is named 'E (eV)'
    df.rename(columns={df.columns[0]: 'E (eV)'}, inplace=True)
    
    # Filter data based on the specified energy range
    df_filtered = df[(df['E (eV)'] >= energy_min) & (df['E (eV)'] <= energy_max)]
    
    return df_filtered

def plot_pdos_3d(df):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Remove grids and make panes transparent
    ax.grid(False)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.set_alpha(0.0)
        axis.pane.set_edgecolor('w')

    # Energy values (Y-axis)
    energies = df['E (eV)'].values
    
    # Define colors from a professional colormap
    colors = cm.viridis(np.linspace(0, 1, len(df.columns) - 1))
    
    # Plot PDOS on vertical planes with filled surfaces
    for i, col in enumerate(df.columns[1:]):
        pdos_values = df[col].values
        x_values = np.full_like(pdos_values, i)  # X-axis now represents orbitals
        
        # Plot transparent filled surface
        X = np.vstack([x_values, x_values])
        Y = np.vstack([energies, energies])
        Z = np.vstack([pdos_values, np.zeros_like(pdos_values)])
        ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.1, linewidth=0, antialiased=True)
        
        # Plot solid line on top
        ax.plot(x_values, energies, pdos_values, color=colors[i], alpha=0.9)

    # Labels and formatting
    ax.set_xlabel('Orbital', fontsize=14, labelpad=10)  # X-axis now represents orbitals
    ax.set_ylabel('Energy (eV)', fontsize=14, labelpad=10, weight='bold')  # Y-axis now represents energy (bold)
    ax.set_zlabel('PDOS', fontsize=14, labelpad=10, rotation=90)  # Z-axis label rotated by 90 degrees
    
    # Set X-axis ticks and labels (orbitals)
    ax.set_xticks(range(len(df.columns[1:])))
    x_tick_labels = df.columns[1:]
    ax.set_xticklabels(x_tick_labels, fontsize=12, rotation=45, ha='right', va='center')  # Diagonal labels
    
    # Only label curves at the width axis where they begin
    for i, col in enumerate(df.columns[1:]):
        ax.text(i, energies[0], df[col].values[0], col, fontsize=12, color=colors[i], 
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.2'))
    
    # Set axis limits to create a box around the plot
    ax.set_xlim(0, len(df.columns[1:]) - 1)  # X-axis limits (orbitals)
    ax.set_ylim(energies.min(), energies.max())  # Y-axis limits (energy)
    ax.set_zlim(0, df.iloc[:, 1:].values.max())  # Z-axis limits (PDOS)
    
    # Draw parallel lines to axes to create a 3D box
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    zlim = ax.get_zlim()
    
    # Draw lines along the edges of the box
    # Vertical lines (Z-axis)
    ax.plot([xlim[0], xlim[0]], [ylim[0], ylim[0]], [zlim[0], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Back left
    ax.plot([xlim[1], xlim[1]], [ylim[0], ylim[0]], [zlim[0], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Back right
    ax.plot([xlim[0], xlim[0]], [ylim[1], ylim[1]], [zlim[0], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Front left
    ax.plot([xlim[1], xlim[1]], [ylim[1], ylim[1]], [zlim[0], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Front right
    
    # Horizontal lines (X-axis and Y-axis)
    ax.plot([xlim[0], xlim[1]], [ylim[0], ylim[0]], [zlim[0], zlim[0]], color='black', linestyle='-', alpha=1.0)  # Bottom back
    ax.plot([xlim[0], xlim[1]], [ylim[1], ylim[1]], [zlim[0], zlim[0]], color='black', linestyle='-', alpha=1.0)  # Bottom front
    ax.plot([xlim[0], xlim[0]], [ylim[0], ylim[1]], [zlim[0], zlim[0]], color='black', linestyle='-', alpha=1.0)  # Bottom left
    ax.plot([xlim[1], xlim[1]], [ylim[0], ylim[1]], [zlim[0], zlim[0]], color='black', linestyle='-', alpha=1.0)  # Bottom right
    
    # Close the top of the box
    ax.plot([xlim[0], xlim[1]], [ylim[0], ylim[0]], [zlim[1], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Top back
    ax.plot([xlim[0], xlim[1]], [ylim[1], ylim[1]], [zlim[1], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Top front
    ax.plot([xlim[0], xlim[0]], [ylim[0], ylim[1]], [zlim[1], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Top left
    ax.plot([xlim[1], xlim[1]], [ylim[0], ylim[1]], [zlim[1], zlim[1]], color='black', linestyle='-', alpha=1.0)  # Top right
    
    # Adjust viewing angle for better perspective
    ax.view_init(elev=20, azim=-45)  # elev = elevation angle, azim = azimuth angle
    
    plt.title('Projected Density of States (PDOS)', fontsize=16, pad=20)  # Increased font size and padding
    plt.tight_layout()
    plt.show()
#----------------------------------------Modify Below This Line-----------------------------------------------------------------------------

# Example usage
file_path = '/content/pdos.xlsx'  # Replace with your actual file
energy_min = 16
energy_max = 20

# Process data and plot
df_filtered = read_and_filter_pdos(file_path, energy_min, energy_max)
plot_pdos_3d(df_filtered)
