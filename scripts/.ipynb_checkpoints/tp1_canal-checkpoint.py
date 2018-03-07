"""
tp1_canal.py
=================
Functions and results of TP2 : Flow in channel

27/03/2018
Miguel Calpe Linares

"""
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

from scripts.tp_base import TPBase

class TP1Canal(TPBase):
    def __init__(self, name=None, HAS_TO_SAVE=False):
        super(TP1Canal, self).__init__()
        self.tag = '_tp1_'
        self.width_canal = 0.04 # width canal in m
        self.name = name
        self.HAS_TO_SAVE = HAS_TO_SAVE
        
    def compute_water_charge(self, volume, time, units_volume='ml'):
        """Computes water charge (m^3/s) from volume in ml 
        and time in seconds.
        """
        if units_volume == 'ml':
            volume_iu = volume / 1e6
        else:
            raise NotImplementedError
    
        return  volume_iu / time

    def compute_energy(self, charge, h):
        """ . """
        rho = self.rho
        g = self.gravity
        d = self.width_canal
        ek = 0.5 * rho * ((charge**2) / (h*d)**2)
        ep = rho * g * h
        return ek + ep

    def compute_froude(self, charge, h):
        """ . """
        g = self.gravity
        d = self.width_canal
        denom = h *d * np.sqrt(h * g)
        return charge / denom


if __name__ == '__main__':

    # Create object TP1Canal
    tp = TP1Canal(name='calpe', HAS_TO_SAVE=True)

    ## QUESTION 1.1 : Mesure water charge & incertitude
    volumes = [550, 600, 650]    # in ml
    times = [2.8, 2.93, 3.]  # in seconds

    charges = []

    for index, volume in enumerate(volumes):
        q = tp.compute_water_charge(
            volume, times[index], units_volume='ml')
        charges.append(q)

    charge = np.mean(charges)
    print('The water charge question 1.1 measured is {} m^3/s'.format(charge))

    # Compute incertitude of the first value of Q
    # dv = 10 ml ; dt = 0.5s
    incert_q = 10 / volumes[0] + 0.5 / times[0]
    
    to_write = (
        'Question 1.1 \n' +
        'Q = {} m3/s \n'.format(np.mean(charges)) +
        'incert_q = {} \n'.format(incert_q))

    ## QUESTION 2.1: Mesure h(x)
    hs = [0.025, 0.023, 0.02, 0.018, 0.015]  # in m

    ## QUESTION 2.2: Mesure E(x)
    energies = []
    for h in hs:
        energies.append(tp.compute_energy(charge, h))

    froudes = []
    for h in hs:
        froudes.append(tp.compute_froude(charge, h))

    fig, ax = plt.subplots()
    ax.plot(energies, hs)

    to_write += (
        'Question 2.1 and 2.2 \n' +
        'h = {} m \n'.format(hs) +
        'energies = {} \n'.format(energies) +
        'froudes = {} \n'.format(froudes))


    ## QUESTION 3.5: Ressaut hydraulique
    # Compute water charge modified
    volumes = [480, 580, 430] # volumes in ml
    times = [3, 3.8, 2.8] # times in seconds

    charges = []

    for index, volume in enumerate(volumes):
        q = tp.compute_water_charge(
            volume, times[index], units_volume='ml')
        charges.append(q)

    charge = np.mean(charges)
    print('The water charge question 3.5 measured is {} m^3/s'.format(charge))
    
    # Compute Froude
    h_amont = 0.032 # in m
    h_aval = 0.008 # in m
    froude_amont = tp.compute_froude(charge, h_amont)
    froude_aval = tp.compute_froude(charge, h_aval)
    
    to_write += (
        'Question 3.5 \n' +
        'Q = {} m3/s \n'.format(charge) +
        'froude_amont = {}'.format(froude_amont) +
        'froude_aval = {}'.format(froude_aval))

    ## Question 3.8;
    hs = [0.032, 0.008, 0.017]
    energies = []
    froudes = []
    for h in hs:
        energies.append(tp.compute_energy(charge, h))
        froudes.append(tp.compute_froude(charge, h))
    
    if tp.HAS_TO_SAVE:
        tp.write_results_to_txt(to_write)

    plt.show()
        
    
    

    
