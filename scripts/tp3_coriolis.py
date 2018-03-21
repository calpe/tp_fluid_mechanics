"""
tp3_coriolis.py
=========

Functions and results TP3: Force de Coriolis

03/03/2018
Miguel Calpe Linares

# TO CHECK: 
Moment computed with force == Moment computed with expression?

# TO DO:
Doc for functions
Code functions to plot from results file .txt
"""
from __future__ import print_function

from math import pi
import matplotlib.pyplot as plt

from scripts.tp_base import TPBase


class TP3Coriolis(TPBase):
    def __init__(self, name=None, HAS_TO_SAVE=False):
        super(TP3Coriolis, self).__init__()
        self.tag = '_tp3_'
        self.l_tube = 0.290 # length of the tube in m
        self.r_disk = 0.102 # radius disk in m
        self.diameter_tube = 0.012 # diameter tube in m
        self.surf_tube = pi * (self.diameter_tube**2) / 4 
        self.name = name
        self.HAS_TO_SAVE = HAS_TO_SAVE
        if self.HAS_TO_SAVE and not self.name:
            raise ValueError('If HAS_TO_SAVE, give your name to save results!')
        
    def compute_moment_coriolis(self, charge, omega):
        """Compute moment of coriolis with the expression:
        M = rho * q * omega * l_tube**2
        """
        g = self.gravity
        rho = self.rho
        l_tube = self.l_tube
        
        # Convert units to units of the international system
        q = self.convert_charge_to(
            charge, to_units='m3/s', from_units='l/min')
        w = self.convert_angular_velocity_to(
            omega, to_units='1/s', from_units='rpm')

        return q * w * rho * l_tube**2

    def compute_height_from_expression(self, charge, omega):
        """ . """
        
        # Define parameters
        g = self.gravity
        surf_tube = self.surf_tube
        l_tube = self.l_tube

        # Convert units to units of the international system
        q = self.convert_charge_to(
            charge, to_units='m3/s', from_units='l/min')
        w = self.convert_angular_velocity_to(
            omega, to_units='1/s', from_units='rpm')
        
        coef_a = 0.5 * (1. / g) * (q**2 / (4 * surf_tube**2))
        coef_b = 0.5 * (1. / g) * (l_tube**2) * w**2
        
        return coef_a - coef_b

    def complete_to_write(self, charge, omegas, forces, hs, moment):
        """ . """
        to_write = (
            'charge = {} l/min \n'.format(charge) +
            'omegas = {} rpm \n'.format(omegas) +
            'forces = {} N \n'.format(forces) +
            'height = {} m \n'.format(hs) +
            'moment_theo = {} Nm \n'.format(moment))
        return to_write

        
if __name__ == '__main__':
    
    # Create object TP Coriolis.
    # Give your name and indicate if you want to save the results
    tp = TP3Coriolis(name='calpe', HAS_TO_SAVE=True)

    # Compute moment Coriolis with constant water charge and
    # different values of angular velocity & compute height from expression.
    charges = [10] # in l /min
    omegas = [85, 96, 110.5, 120] # in rpm for a constant charge
    forces = [1.47, 1.7, 2.0, 2.2] # in N
    hs = [0.45, 0.39, 0.25, 0.166] # in m
    #############################
    #############################
    
    moment_theor = []
    moment_meas = []
    hs_theor = []
    for charge in charges:
        for i, omega in enumerate(omegas):
            moment_theor.append(tp.compute_moment_coriolis(charge, omega))
            moment_meas.append(forces[i] * tp.r_disk)
            hs_theor.append(2  * tp.compute_height_from_expression(charge, omega))
            
    to_write = (
        'Moment Coriolis from omegas \n' +
        tp.complete_to_write(charge, omegas, forces, hs, moment_theor) +
        'moment_meas = {} Nm \n'.format(moment_meas) +
        'hs_theor = {} m \n'.format(hs_theor) +
        '************************** \n')

    # Plot Moment Coriolis Vs omegas
    fig1, ax1 = plt.subplots()
    ax1.set_title('Moment coriolis Vs Angular velocity')
    ax1.set_xlabel(r'$\omega (s^{-1})$')
    ax1.set_ylabel(r'$M_{coriolis} (Nm)$')

    # Plot Moment Coriolis Vs omegas
    fig2, ax2 = plt.subplots()
    ax2.set_title('Height Vs Angular velocity')
    ax2.set_xlabel(r'$\omega (s^{-1})$')
    ax2.set_ylabel(r'$H (m)$')
    

    omegas_si = []
    for omega in omegas:
        omegas_si.append(omega/60.)
    ax1.plot(omegas_si, moment_theor, label='theory')

    ax2.plot(omegas_si, hs, label='measured')
    ax2.plot(omegas_si, hs_theor, color='k', label='theory')

    ax2.legend()

    # Compute moment Coriolis with constant angular velocity and
    # different values of water charge.
    omegas = [120] # in rpm
    charges = [11.5, 12, 12.5] # in l/min
    forces = [2.3, 2.4, 2.5] # in N
    hs = [0.263, 0.375, 0.5] # in m
    ##########################
    ##########################
    
    moment_theor = []
    moment_meas = []
    for omega in omegas:
        for i, charge in enumerate(charges):
            moment_theor.append(tp.compute_moment_coriolis(charge, omega))
            moment_meas.append(forces[i] * tp.r_disk)

    to_write += (
        'Moment Coriolis from charges \n' +
        tp.complete_to_write(charge, omegas, forces, hs, moment_theor) +
        'moment_meas = {} Nm \n'.format(moment_meas) +
        '************************** \n')

    # Plot Moment Coriolis Vs charges
    fig3, ax3 = plt.subplots()
    ax3.set_title('Moment coriolis Vs Charge')
    ax3.set_xlabel(r'$q (m^{3}/s)$')
    ax3.set_ylabel(r'$M_{coriolis} (Nm)$')

    charges_si = []
    for charge in charges:
        charges_si.append(charge / 60. / 1000.)
    ax3.plot(charges_si, moment_theor, label='theory')

    if tp.HAS_TO_SAVE:
        tp.write_results_to_txt(to_write)

    plt.show()

