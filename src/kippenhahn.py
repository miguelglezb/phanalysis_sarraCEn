#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sarracen as sar
from utils.rdumpfiles import read_dumpfiles
from utils.vector_math import recentre_from_sink
import matplotlib.pyplot as plt
import numpy as np
import dataread as dr
from pformat import plot_format

def bins_range(dumpfile_list,bmin=1):
    sdf, sdf_sinks = sar.read_phantom(dumpfile_list[-1])
    [x1, y1, z1] = recentre_from_sink(sdf,sdf_sinks,sink=0)    
    max_r = np.sqrt(x1**2 + y1**2 + z1**2).max()
    return np.logspace(bmin, np.log10(max_r),100)

def kipp_mean(dumpfile_list,bmin=1.0,weight='rho'):
    '''
    Generates a pair of arrays to generate a Kippenhahn diagram of the
    common envelope with a quantity weight  
        
    Parameters
    ----------
    dumpfile_list : list
       list of paths of the dumpfiles of the simulation.
    bmin : float, default='1.0'
        Minimum value for the radius/mass coordinate.
    weight : str, default='rho'
        Quantity to be represented in the diagram, 
        should be in sdf.keys()
    Returns
    -------
    Pair of numpy arrays.

    '''
    bins = bins_range(dumpfile_list,bmin) 
    time, vcolumn = [], []
    for file in dumpfile_list:
        vcolumn.append([])
        bini = bins[0]
        sdf, sdf_sinks = sar.read_phantom(file)
        t = sdf.params['time']*dr.constants.yr
        sdf.calc_density()
        [x1, y1, z1] = recentre_from_sink(sdf,sdf_sinks,sink=0)
        sdf['r'] = np.sqrt(x1**2 + y1**2 + z1**2)
        for b in bins[1:]:
            cellval = sdf[sdf['r'].between(bini,b)][weight].mean()
            cellval = np.log10(cellval)
            bini = b
            vcolumn[-1].append(cellval)
        print(round(t,2))
        time.append(t)
    return (vcolumn,time)    



if __name__ == "__main__":
    path_dumpfiles = '/media/miguelgb/drive2/Dust/Datafiles/A_tccclsax_boundmax/'
    dump_list = read_dumpfiles(path=path_dumpfiles)
    ph_data = dr.phantom_evdata('data/external/separation_vs_time.ev')
    dump_list = read_dumpfiles(path=path_dumpfiles)
    bins = bins_range(dump_list,bmin=1.5)
    rhomean, time = kipp(dump_list,bmin=1.5)
    X, Y = np.meshgrid(time, bins[1:])
    Z = []
    for y in enumerate(bins[1:]):
        Z.append([])
        for x in enumerate(time):
            Z[-1].append(rhomean[x[0]][y[0]])      

    fig,ax=plt.subplots(1,1)
    plt.contourf(X, np.log10(Y), Z, cmap=plt.cm.magma)
    plot_format('time [yr]', 'log r [R${_\odot}$]',leg=False)
    #plt.title('No dust')
    cb = plt.colorbar()
    #plt.clim(0,1.05E39)
    plt.xlim(0,5000*50*dr.constants.yr)
    cb.ax.set_ylabel('[K]', rotation=270, fontsize=15)
    cb.ax.get_yaxis().labelpad = 18
    for t in cb.ax.get_yticklabels():
         t.set_fontsize(18)
    plt.show()