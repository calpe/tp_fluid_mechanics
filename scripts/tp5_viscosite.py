"""
tp5_viscosite.py
================

Functions TP5: Viscosité.

27/03/2018
Miguel Calpe Linares
"""

from __future__ import print_function

from scripts.tp_base import TPBase

class TP5Viscosite(TPBase):
    def __init__(self):
        super(TP5Viscosite, self).__init__()
        self.tag = '_tp5_'
        self.rayon_capillaire = 0.235e-3 # rayon capillaire en m
        self.volume = 5e-6 # volume en m3

    def compute_reynolds(self, time, viscosity):
        """
        Calcule le nombre de Reynolds à partir temps et viscosité mesuré.
        
        Parameters
        ----------
        viscosity : float
          Viscosité mesuré m2/s
        
        time : float
          Temps en s
        """
        d = 2 * self.rayon_capillaire
        v = self.volume
        nu = viscosity
        t = time
        
        return (4 * v) / (viscosity * t * pi * d)
