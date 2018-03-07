"""
tp1_canal.py
=================
Functions for TP1. Ecoulement en canal

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
        """
        Computes water charge (m^3/s) from volume in ml 
        and time in seconds.
        """
        if units_volume == 'ml':
            volume_iu = volume / 1e6
        else:
            raise NotImplementedError
    
        return  volume_iu / time

    def compute_energy(self, charge, h):
        """ 
        Computes energy with the expression:
        E = 0.5 * rho * (Q**2 / (h * d)**2) + rho * g * h
        """
        rho = self.rho
        g = self.gravity
        d = self.width_canal
        ek = 0.5 * rho * ((charge**2) / (h*d)**2)
        ep = rho * g * h
        return ek + ep

    def compute_froude(self, charge, h):
        """ 
        Computes the froude number as 
        Fr = (Q / (h * d)) * (1 / np.sqrt(g * h))
        """
        g = self.gravity
        d = self.width_canal
        denom = h *d * np.sqrt(h * g)
        return charge / denom
