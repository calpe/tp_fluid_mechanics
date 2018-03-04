"""
scripts_canal.py
==========
Functions and results of TP2 : Flow in channel

27/03/2018
Miguel Calpe Linares

"""
from __future__ import print_function

import numpy as np

from tp_base import TPBase

class TP1Canal(TPBase):
    def __init__(self, name=None, HAS_TO_SAVE=False):
        super(TP1Canal, self).__init__()
        self.tag = '_tp1_'
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


if __name__ == '__main__':

    # Create object TP1Canal
    tp = TP1Canal(name='calpe', HAS_TO_SAVE=True)

    ## QUESTION 1.1 : Mesure water charge
    volumes = [550, 600, 650]    # in ml
    times = [2.8, 2.93, 3.]  # in seconds

    charges = []

    for index, volume in enumerate(volumes):
        q = tp.compute_water_charge(
            volume, times[index], units_volume='ml')
        charges.append(q)

    charge = np.mean(charges)
    print('The water charge question 1.1 measured is {} m^3/s'.format(charge))

    to_write = (
        'Question 1.1 \n' +
        'Q = {} m3/s \n'.format(np.mean(charges)))

    tp.write_results_to_txt(to_write)

    ## QUESTION 3.5
    dx = 1 # in meters
    time = 3.85 # in seconds
    h = 0.022 # m
    d = 0.04 # m

    vel = dx / time
    surf = h * d
    q = vel * surf
    print ('The water charge question 3.5 is {} m^3/s'.format(q))

    to_write += (
        'Question 3.5 \n' +
        'Q = {} m3/s \n'.format(q))

    if tp.HAS_TO_SAVE:
        tp.write_results_to_txt(to_write)
    
    # # Compute water charge question 3.5 (values Philippe)
    # dx = 1 # in meters
    # time = 3.85 # in seconds
    # h = 0.022 # m
    # d = 0.04 # m

    # vel = dx / time
    # surf = h * d
    # q = vel * surf
    # print ('The water charge question 3.5 is {} m^3/s'.format(q))


    # # Compute question 3.8
    # h = [0.018, 0.007, 0.032]
    # d = 0.04 # in meters
    # surf = []
    # for value in h:
    #     surf.append(value * d)
    # vel = []
    # for value in surf:
    #     vel.append(q/value)
    # froudes = []
    # for i in range(len(vel)):
    #     froudes.append(vel[i]/np.sqrt(gravity * h[i]))

    # print('The froude number for different values of h  are {}'.format(froudes))

    # # Compute energies
    # energies = []
    # for i in range(len(vel)):
    #     print(vel[i])
    #     energy = 0.5 * rho * vel[i]**2 + rho * gravity * h[i]
    #     energies.append(energy)
        
    # print('The values of energy are {}'.format(energies))
    
    
    

    
