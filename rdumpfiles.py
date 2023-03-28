#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dataread as dr
import sarracen as sar
import os

def read_dumpfiles(files_sufix='binary_', path='./', evy_nfile=-1):
    '''
    Creates a list of the dumpfiles that will be used in the analysis.
        
    Parameters
    ----------
    files_sufix : str, default='binary_'
        Prefix of the dumpfiles  
    path : str, default='./'
        Path of the dumpfiles
    evy_files : integer, default='-1'
        If -1, it will take the path of every single dumpfile with
        files_sufix in the path. For any other positive integer, it
        will take every evy_files to generate the list
    Returns
    -------
    List of strings (dumpfile names, including path)

    '''
    os.system('ls ' + path + files_sufix + '* > listfiles.txt')
    openlist = open('listfiles.txt')
    if evy_nfile==-1:
        list_dumpfiles = openlist.read().splitlines()
    else:
        list_dumpfiles = openlist.read().splitlines()[::evy_nfile] 
    openlist.close()
    os.system('rm listfiles.txt')          
    return list_dumpfiles

