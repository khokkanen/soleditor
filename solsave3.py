#!/usr/bin/python

import sys
import yaml
from pyamf import sol, AMF3

infile = open(str(sys.argv[1]), "r")
solfile = str(sys.argv[2])
lsodata = yaml.load(infile)
sol.save(lsodata, solfile, encoding=AMF3)
infile.close()
