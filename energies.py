#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import dataread as dr
from matplotlib import rc
from matplotlib import rcParams
import sarracen as sar
from rdumpfiles import read_dumpfiles
from separation import sep_t

path_dumpfiles = '/media/miguelgb/drive2/Dust/Datafiles/A_ccc/'
dump_list = read_dumpfiles(path=path_dumpfiles)

def tot_potential(dumpfile_list):
    time = np.array([])
    potential = np.array([])
    for dump in dumpfile_list:
        file_name = dump.split('/',-1)[-1]
        sdf, sdf_sinks = sar.read_phantom(dump)
        particlemass = sdf.params['mass']
        x1 = sdf['x'] - sdf_sinks['x'][0]
        y1 = sdf['y'] - sdf_sinks['y'][0]
        z1 = sdf['z'] - sdf_sinks['z'][0]
        x2 = sdf['x'] - sdf_sinks['x'][1]
        y2 = sdf['y'] - sdf_sinks['y'][1]
        z2 = sdf['z'] - sdf_sinks['z'][1]
        x_sinks = sdf_sinks['x'][1] - sdf_sinks['x'][0]
        y_sinks = sdf_sinks['y'][1] - sdf_sinks['y'][0]
        z_sinks = sdf_sinks['z'][1] - sdf_sinks['z'][0]
        r_sinks = np.sqrt(x_sinks**2 + y_sinks**2 + z_sinks**2)
        r1 = np.sqrt(x1**2 + y1**2 + z1**2)
        r2 = np.sqrt(x2**2 + y2**2 + z2**2)
        phi = - (sdf_sinks['m'][0]/r1).sum() - (sdf_sinks['m'][1]/r2).sum()
        pot_bet_sinks = -(sdf_sinks['m'][0]*sdf_sinks['m'][1])/r_sinks
        #potential = np.append(potential, particlemass*phi + sdf['poten'].sum() + pot_bet_sinks)
        potential = np.append(potential, pot_bet_sinks)
        time = np.append(time,sdf.params['time'])
        print('file: ',file_name)
    return time, potential

