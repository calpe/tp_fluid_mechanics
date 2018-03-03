"""
tp3_coriolis.py
=========

Functions and results TP3: Force de Coriolis

03/03/2018
Miguel Calpe Linares

"""

from __future__ import print_function

import  matplotlib.pyplot as plt
from math import pi

# Question 1.7 and 1.8
# Water charge mesure from graph
charge = 1.6e-4 # in m^3 / s

# Mesures
omegas = [85, 96, 110.5, 120] # in rpm for a constant charge
forces = [1.47, 1.7, 2.0, 2.2] # in N
hs = [0.45, 0.39, 0.25, 0.166] # in m

def convert_rpm_to(mesure, convert_to='rad/s'):
    """ Convert mesure from rpm to ..."""
    if convert_to == 'rad/s':
        return mesure * (2 * pi) / 60.
    elif convert_to == '1/s':
        return mesure / 60.
    else:
        raise NotImplementedError(
            'Units {} not yet implemented'.format(convert_to))

def compute_moment_from_force(force, r_disk=0.102):
    """ Compute moment from measured force. 
    Parameters
    ----------------
    force : float
      Force in Newtons
    
    r_disk : float
      Radius of the disk

    Return
    ---------
    Moment : int
      Moment of the force in Nm
    """
    return force * r_disk

def compute_moment_coriolis(omega, charge, l_tube=0.290, rho=1000.):
    """ Compute moment force coriolis from omega and charge 
    with the expression: M = omega * charge * rho * l_tube**2
    
    Parameters
    ----------------
    omega : float
      Angular velocity in s^-1
    
    charge : float
      Water charge in m^3/s

    l_tube : float
      Length of the tube in meters

    rho : float
     Water density in kg/m^3
    """
    omega = convert_rpm_to(omega, convert_to='1/s')
    return omega * charge * rho * l_tube**2


# Question 1.7
# Compute moments from omegas and constant charge 
charge = 1.6e-4 # in m^3 / s
omegas = [85, 96, 110.5, 120] # in rpm for a constant charge
moment_omega = []
for omega in omegas:
    moment_omega.append(compute_moment_coriolis(omega, charge))

fig1, ax1 = plt.subplots()
ax1.plot(omegas, moment_omega)
ax1.set_xlabel('$\omega (rpm)$')
ax1.set_ylabel('$M (Nm)$')  
plt.show()
