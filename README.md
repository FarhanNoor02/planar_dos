# planar_dos.py
A python script to produce publication quality 3D plot showing the atom projected density of states (computed by DFT codes) of a material in different vertical planes of the figure:
![plot](https://github.com/FarhanNoor02/planar_dos/blob/main/dos_trial.png) 

# How To Use:

1)The atom projected DOS are computed via DFT codes such as VASP(6.x.x) or Quantum ESPRESSO(7.3) and should be collected in a single file named dos_trial.xlsx in the form:

![plot2](https://github.com/FarhanNoor02/planar_dos/blob/main/planar_dos1.PNG) 

2) Here, the first column is always Energy
3) After the nergy column, one can add as many columns as calculated/needed, and ensure proper column names as these column heading will be the labels on the horizontal axis
4) Run this script in the directory where the dos_trial.xlsx file is saved.
