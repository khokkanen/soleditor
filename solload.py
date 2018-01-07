#!/usr/bin/python

import sys
import yaml
from pyamf import sol, AMF3

solfile = str(sys.argv[1])
outfile = open(str(sys.argv[2]), "w")
lsodata = sol.load(solfile)
yaml.dump(lsodata, outfile, default_flow_style=False)
outfile.close()
