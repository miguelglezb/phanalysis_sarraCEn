#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sarracen as sar
import numpy as np
from utils.rdumpfiles import read_dumpfiles
from utils.vector_math import recentre_from_sink


def calc_kappa_bowen(T_eq,kap_max=5,dT=50,T_cond=1500,kap_min=1E-4):
    '''
    Calculates Bowen opacity as function of equilibrium temperature. 
    Parameters
    ----------
    T_eq : float, array
        Equilibrium temperature. It can be used to calculate for a single value,
        for an array or a full sdf column.  
    kap_max : float, default='5.'
        Maximum value of opacity.
    dT : float, default='50.'
        Condensation temperature range
    T_cond : float, default='1500.'
        Condensation temperature   
    Returns
    -------
    Pair of numpy arrays.

    '''

    kappa = kap_min + kap_max/(1+np.exp((T_eq - T_cond)/dT))
    return kappa