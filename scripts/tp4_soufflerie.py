"""
tp4_soufflerie.py
==================

Parameters, functions and results TP4: Wind tunnel

06/03/2017
Miguel Calpe Linares

# TODO:
-------
Implement diameter disk

# Notes
--------
Force over an object:
F = 0.5 * C * rho * U**2 * S 

C : Non-dimensional number
rho : density in kg/m3
U : fluid velocity in m/s
S : Front surface (for a sphere is pi * R**2)

Drag force over a wing: 
F = 0.5 * C(alpha) * rho * U**2 * L * sin(alpha) * d

alpha : wing angle
L : length of the wing
d = width of the wing

Portant force over a wing: 
F = 0.5 * C(alpha) * rho * U**2 * L * cos(alpha) * d

Drag coefficient for disk and sphere = cte
Drag and portant coefficient wing = depends on angle
"""

from __future__ import print_function

from scripts.tp_base import TPBase

class TP4Soufflerie(TPBase):
    def __init__(self, name=None, HAS_TO_SAVE=False):
        super(TP4Soufflerie, self).__init__()
        self.tag = '_tp4_'
        self.nu = 1e-6 # in m2/s
        self.surf_disk = None # Not implemented
        self.surf_sphere = None # Not implemented
        self.diam_disk = None
        self.length_wing = None
        self.width_wing = None
        self.HAS_TO_SAVE = HAS_TO_SAVE

    def compute_reynolds(self, velocity, diameter):
        """ Computes Reynolds number as U * D / nu. """
        return velocity * diameter / self.nu

    def compute_drag_coef(
            self, force, velocity, surface, profile='disk'):
        """ Computes drag force for the different profiles"""
        rho = self.rho
        if profile == 'disk':
            surf = self.surf_disk
        elif profile == 'sphere':
            surf = self.surf_sphere
        else:
            raise NotImplementedError(
                'Profile {} is not implemented.'.format(profile))

        return (2 * force) / (surf * rho * velocity**2)

if __name__ == '__main__':

    # Initialize object tp
    tp = TP4Soufflerie(name='calpe', HAS_TO_SAVE=False)
    
    # QUESTION 1.2: Mesure drag force for disk
    forces = [0.07, 0.13, 0.26] # in N
    vels = [2.6, 4.7, 6.6] # in m/s
    delta_vel = 0.1 # in m/s (max precision of the tool)
    delta_f = 0.01 # in N 

    incert_vels = []
    incert_force = []
    for i, vel in enumerate(vels):
        incert_vels.append(delta_vel / vel)
        incert_force.append(delta_f / forces[i])

    to_write = ('Question 1.2 \n' + 
                'f_drag = {} N \n'.format(forces) +
                'vel_drag = {} m/s \n'.format(vels) +
                'incert_vel = {} \n'.format(incert_vels) +
                'incert_force = {} \n'.format(incert_force))
    
    # QUESTION 1.3: Reynolds for the disk
    reynolds = []

    # QUESTION 1.4: Compute drag coefficient.
    # coef_drag ~ 1 (disk)

    # QUESTION 1.5: Same previous computations as for the disk.

    # QUESTION 2.2:
    angles = [0, 3, 8, -8] # angle in degrees
    vels = [7.5, 7.2, 7, 7.3] # velocity in m/s
    f_drag = [0.1, 0.17, 0.42, 0.22] # draf force in N
    f_port = [0.6, 1, 2.1, -0.9] # portant force in N

    
    # To write results into a file.
    if self.HAS_TO_SAVE:
        tp.write_results_to_txt(to_write)
    
