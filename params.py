"""
Module containing the constants needed for the numerical solution of the laplace equation.
"""

# DIMENSIONS OF THE PLATES [CM]

l_y = 5     # Side 1
l_z = 10    # Side 2
d = 1       # Separation in between plates

# DIMENSIONS OF THE BOX [CM]

L_X = 10
L_Y = 15
L_Z = 30

# POTENTIALS [V]

V_1 = 10
V_2 = -5

# MESHING PARAMETERS

ds = 0.1

x_min = -5
x_max = 5
M_X = 101

y_min = -7.5
y_max = 7.5
M_Y = 151

z_min = -15
z_max = 15
M_Z = 301

r_tol = 10e-2
