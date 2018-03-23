"""
tp2_vidange.py
==============

Functions and results of TP2: Vidange d'un reservoir

06/03/2017
Miguel Calpe Linares

"""
from __future__ import print_function

from math import pi
from scripts.tp_base import TPBase

class TP2Vidange(TPBase):
    def __init__(self, name=None, HAS_TO_SAVE=False):
        super(TP2Vidange, self).__init__()
        self.diam_small = 0.003 # Small diameter in m.
        self.surf_small = pi * (self.diam_small**2 / 4) # Surface small in m^2
        self.surf_big = 79.3 / 1e4 # Surface big in m^2
