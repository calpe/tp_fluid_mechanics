from __future__ import print_function

import os
from math import pi

class TPBase(object):
    def __init__(self):
        self.gravity = 9.8 # gravity in m3/s
        self.rho = 1000 # water density in kg/m3
        self.tag = None
        self.name = None

    def convert_angular_velocity_to(self, value, to_units, from_units='rpm'):
        """ Convert angular velocity from given units to given units """
        if from_units == 'rpm':
            if to_units == 'rad/s':
                return value * (2 * pi) / 60.
            elif to_units == '1/s':
                return value / 60.
            else:
                raise NotImplementedError('Units {} not implemented'.format(
                    to_units))
        else:
            raise NotImplementedError('Units {} not implemented'.format(
                from_units))

    def convert_charge_to(self, value, to_units, from_units):
        """ . """
        if from_units == 'l/min':
            if to_units == 'm3/s':
                return value / 1000. / 60.
            else:
                raise NotImplementedError('Units {} not implemented'.format(
                    to_units))
        else:
            raise NotImplementedError('Units {} not implemented'.format(
                from_units))

    
    def write_results_to_txt(self, to_write):
        """ Write results to file .txt """
        name_file = 'results' + self.tag + self.name + '.txt'
        if os.path.exists(name_file):
            with open(name_file, 'r+') as f:
                f.write(to_write)
        else:
            with open(name_file, 'w') as f:
                head = ' ***** {} ***** \n'.format(name_file)
                f.write(head + to_write)

