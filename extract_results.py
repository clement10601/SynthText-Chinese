# Author: Ankush Gupta
# Date: 2015

"""
Visualize the generated localization synthetic
data stored in h5 data-bases
"""
from __future__ import division
import io
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt 
import h5py 
from common import *
import string
import random
from PIL import Image

OUT_FOLD = 'output'
anno_fold = 'annotations'
img_fold = 'images'

def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def save_textbb(fid, out_fold ,text_im, charBB_list, wordBB, txt, alpha=1.0):
    """
    text_im : image containing text
    charBB_list : list of 2x4xn_i bounding-box matrices
    wordBB : 2x4xm matrix of word coordinates
    """
    image = Image.fromarray(np.uint8(text_im))
    sfp = os.path.join(OUT_FOLD, img_fold)
    image.save(os.path.join(sfp, fid+'.jpg'))
    H,W = text_im.shape[:2]
    txt_out = []
    for t in txt:
        txt_out += t.decode('utf-8').split()
    dimset = []
    # plot the word-BB:
    for i in range(wordBB.shape[-1]):
        bb = wordBB[:,:,i]
        bb = np.c_[bb,bb[:,0]]
        # visualize the indiv vertices:
        xyset = []
        for j in range(4):
            xyset.append(int(bb[0,j]))
            xyset.append(int(bb[1,j]))
        dimset.append(xyset)
    fp = os.path.join(OUT_FOLD, anno_fold)
    afp = os.path.join(fp, fid + '.txt')
    with open(afp, 'w') as f:
        assert len(txt_out) == len(dimset)
        for i in range(len(txt_out)):
            str_out = ','.join(str(x) for x in dimset[i])
            str_out += ',' + txt_out[i]
            f.write('{}\n'.format(str_out))


def main(db_fname, OUT_FOLD):
    db = h5py.File(db_fname, 'r')
    dsets = sorted(db['data'].keys())
    print("total number of images : ", colorize(Color.RED, len(dsets), highlight=True))
    for k in dsets:
        rgb = db['data'][k][...]
        charBB = db['data'][k].attrs['charBB']
        wordBB = db['data'][k].attrs['wordBB']
        txt = db['data'][k].attrs['txt']
        fid = id_generator()
        save_textbb(fid, OUT_FOLD, rgb, [charBB], wordBB, txt)
        print("image name        : ", colorize(Color.RED, k, bold=True))
        print("  ** no. of chars : ", colorize(Color.YELLOW, charBB.shape[-1]))
        print("  ** no. of words : ", colorize(Color.YELLOW, wordBB.shape[-1]))
        print("  ** text         : ", colorize(Color.GREEN, txt))
    db.close()

if __name__=='__main__':
    if not os.path.exists(OUT_FOLD):
        os.makedirs(OUT_FOLD)
    if not os.path.exists(os.path.join(OUT_FOLD, anno_fold)):
        os.makedirs(os.path.join(OUT_FOLD, anno_fold))
        os.makedirs(os.path.join(OUT_FOLD, img_fold))
    main('results/SynthText.h5', OUT_FOLD)

