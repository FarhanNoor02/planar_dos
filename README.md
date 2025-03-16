# Overview
This Python script is designed to generate publication-quality 3D plots for visualizing the atom-projected density of states (PDOS) computed by Density Functional Theory (DFT) codes. The script reads PDOS data from a single Excel file and produces a 3D plot where each orbital-projected DOS is displayed in separate vertical planes. This visualization is particularly useful for researchers and scientists studying the electronic structure of materials, as it provides a clear and intuitive representation of the contributions of different atomic orbitals to the total density of states.

The script is highly customizable, allowing users to adjust the energy range, color schemes, and viewing angles to suit their specific needs. The resulting plots are ideal for inclusion in scientific publications, presentations, and reports.

![screenshot](https://github.com/FarhanNoor02/planar_dos/blob/main/dos_trial.png)

# Key Features
Input Data Format:

The script reads PDOS data from a single Excel file.

The first column of the Excel file must contain the energy values (in eV).

Subsequent columns should contain the orbital-projected DOS data for each orbital.

3D Visualization:

Each orbital-projected DOS is plotted in a separate vertical plane within the 3D plot.

The energy values are plotted along the Y-axis, while the PDOS values are plotted along the Z-axis.

The X-axis represents the different orbitals, with each orbital occupying a distinct vertical plane.

Publication-Quality Output:

The script uses Matplotlib and mpl_toolkits.mplot3d to generate high-quality 3D plots.

Customizable colormaps (e.g., viridis, plasma, inferno) ensure visually appealing and professional-looking plots.

The plot includes axis labels, tick marks, and legends for clarity.

Customization Options:

Users can specify the energy range to focus on specific regions of interest.

The viewing angle of the 3D plot can be adjusted for optimal visualization.

The script supports bold labels, rotated axis labels, and diagonal tick labels for better readability.

Fully Enclosed 3D Box:

The plot is enclosed in a 3D box with dashed lines along the edges, ensuring a clean and professional appearance. As shown above


# Input Data:

The script reads the PDOS data from an Excel file. The first column should contain the energy values, and the subsequent columns should contain the orbital-projected DOS data. The headings of these columns will appear as the labels for the orbital projected DOS inside the 3D plot

# Data Filtering:

Users can specify an energy range to filter the data and focus on specific regions of the density of states.

3D Plot Generation:

The script generates a 3D plot where each orbital-projected DOS is displayed in a separate vertical plane.

The energy values are plotted along the Y-axis, the PDOS values along the Z-axis, and the orbitals along the X-axis.

# Customization:

Users can customize the plot by adjusting the colormap, viewing angle, and axis labels.

Output:

The script outputs a high-quality 3D plot that can be saved as an image file or directly included in publications. As shown Above

# Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

# Keywords
Density of States (DOS), Atom-Projected Density of States (PDOS), 3D Visualization, Python Script, DFT Calculations, Electronic Structure


# Remarks:
The planar_dos.py script has plenty of comments to ensure it is easy to understand the strcutre and develop further.
If you have used this script in rendering publication-quality figures in your work, consider citing this repository.
