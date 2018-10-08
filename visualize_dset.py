# Author: Ankush Gupta
# Date: 2015

"""
Visualize the generated localization synthetic
data stored in h5 data-bases
"""
from __future__ import division
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt 
import h5py 
from common import *


def main(db_fname):
    db = h5py.File(db_fname, 'r')
    print(list(db.keys()))
    db.close()

if __name__=='__main__':
    main('data/dset.h5')

