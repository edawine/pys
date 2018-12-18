#!/usr/bin/sh spcli

from seqpy import cout, cerr, cexit, gzopen
from seqpy.cmds import arg_parser

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import io


def init_argparser(p=None):
    if not p:
        p = arg_parser("ralt2iterqc - iter")
    p.add_argument('--filter', default='')
    p.add_argument('--lmiss', type=float, default=-1)
    p.add_argument('--imiss', type=float, default=-1)
    p.add_argument('--mac', type=int, default=-1)
    p.add_argument('--iter', type=int, default=1)
    p.add_argument('infile')

    return p


def main( args ):

    ralt2iterqc( args )


def ralt2iteqc( args ):

    cerr('[I - reading input files]')

    infile = gzopen(args.infile)
    samples = next(infile).strip().split('\t')
    sample_idx = list(range(len(samples)))
    M = np.loadtxt(infile, delimiter='\t')
    site_idx = list(range(len(samples)))
    cerr('[I - reading %d sites for %d samples' % (len(site_idx), len(sample_idx)))

    for i in range(iter):
        pass
        M, site_idx, sample_idx = filter_lmiss(M, site_idx, sample_idx, args.lmiss)
        M, site_idx, sample_idx = filter_imiss(M, site_idx, sample_idx, args.imiss)
        M, site_idx, sample_idx = filter_mac(M, site_idx, sample_idx, args.mac)


    # filtering order: lmiss > imiss > mac


def check_sanity(M, site_idx, sample_idx):
    # sanity checking
    if len(sample_idx) != shape[1]:
        cexit('[E - inconsistent M shape and no of samples!]')
    if len(site_idx) != shape[0]:
        cexit('[E - inconsistent M shape and no of sites!]')

def filter_lmiss(M, site_idx, sample_idx, lmiss):
    shape = M.shape

    site_missingness = np.count_nonzero(M < 0, axis=1) / len(sample_idx)
    flags = site_missingness < lmiss

    M2 = M[ np.where( flags ) ]
    site_idx2 = site_idx[ np.where( flags ) ]

    return M2, site_idx2, sample_idx


def filter_imiss(M, sample_idx, imiss):
    return M, sample_idx


def filter_mac(M, site_idx, mac):
    return M, site_idx