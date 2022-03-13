"""
Module containing the algorithm for the laplace equation.
"""
import numpy as np
import params as cts

# MESHES

V_x = np.arange(cts.x_min, cts.x_max + cts.ds, cts.ds)
V_y = np.arange(cts.y_min, cts.y_max + cts.ds, cts.ds)
V_z = np.arange(cts.z_min, cts.z_max + cts.ds, cts.ds)
V_matrix = np.zeros((cts.M_X, cts.M_Y, cts.M_Z))

# Set boundary values for the potentials of the plates.
V_matrix[46, 51:102, 101:202] = 10
V_matrix[56, 51:102, 101:202] = -5

