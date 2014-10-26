#!/usr/bin/env python

import subprocess
import os.path
from conf import *

for item in NAVBAR:
    if type(item) is str:
        name = item.split('|')[0]
        outfname = item.split('|')[1]
        cfile = 'content/' + name + '.md'
        if os.path.isfile(cfile):
            with open(outfname, 'w') as of:
                print "Generating: " + outfname
                subprocess.call(["./generator.py", name], stdout=of, shell=False)
    elif type(item) is list:
        for iitem in item[1]:
            name = iitem.split('|')[0]
            outfname = iitem.split('|')[1]
            cfile = 'content/' + name + '.md'
            if os.path.isfile(cfile):
                with open(outfname, 'w') as of:
                    print "Generating: " + outfname
                    subprocess.call(["./generator.py", name], stdout=of, shell=False)

