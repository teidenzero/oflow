from __future__ import print_function

import os, sys, numpy as np
import argparse
from scipy import misc
import tempfile
from math import ceil
import pyexr

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--f")
parser.add_argument("--o")

args = parser.parse_args()
flowFile = args.f
outputFile = args.o


f = open(flowFile, 'rb')

header = f.read(4)
if header.decode("utf-8") != 'PIEH':
    raise Exception('Flow file header does not contain PIEH')

width = np.fromfile(f, np.int32, 1).squeeze()
height = np.fromfile(f, np.int32, 1).squeeze()
flow = np.fromfile(f, np.float32, width * height * 2).reshape((height, width, 2))
u = flow[:, :, 0]
v = flow[:, :, 1]

pyexr.write(outputFile, flow, channel_names=['R','G'])
