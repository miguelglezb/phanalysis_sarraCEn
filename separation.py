#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import dataread as dr
from matplotlib import rc
from matplotlib import rcParams
import sarracen as sar
from rdumpfiles import read_dumpfiles


path_dumpfiles = '/media/miguelgb/drive2/Dust/Datafiles/A_ccc/'
dump_list = read_dumpfiles(path=path_dumpfiles)


def sep_t(dumpfile_list):
    time = np.array([])
    x_sep, y_sep, z_sep = np.array([]), np.array([]), np.array([])
    r_sep = np.array([])
    for dump in dumpfile_list:
        file_name = dump.split('/',-1)[-1]
        sdf, sdf_sinks = sar.read_phantom(dump)
        x_sinks = sdf_sinks['x'][1] - sdf_sinks['x'][0]
        y_sinks = sdf_sinks['y'][1] - sdf_sinks['y'][0]
        z_sinks = sdf_sinks['z'][1] - sdf_sinks['z'][0]
        r = np.sqrt(x_sinks**2 + y_sinks**2 + z_sinks**2)
        x_sep, y_sep, z_sep = np.append(x_sep,x_sinks) , np.array(y_sep,y_sinks), np.array(z_sep,z_sinks)
        r_sep = np.append(r_sep,r)
        time = np.append(time,sdf.params['time'])
        print('file: ',file_name)
    
    return time, x_sep, y_sep, z_sep, r_sep

