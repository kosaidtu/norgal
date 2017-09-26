#!/usr/bin/env python

from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from matplotlib.backends.backend_agg import FigureCanvasAgg
#import matplotlib.numerix as nx


import matplotlib
#matplotlib.use('Agg')
from argparse import ArgumentParser

import sys
myfile = sys.argv[1]


try:
 a = int(sys.argv[2])
except:
 a = -1


i = 0
with open(myfile, "r") as fid:
 L = []
 X = []
 line = fid.readline()
 line = fid.readline().rstrip()
 while line:
  if a != -1 and i>=a:
   break
  i += 1
  L.append(line.split()[-1])
  X.append(line.split()[0])
  line = fid.readline().rstrip()




fig = Figure()
ax = fig.add_subplot(111)
ax.set_title("Khist")
ax.set_xlabel( "Depth")
ax.set_ylabel( "Count")

print(len(X),len(L))

try:
 lim = int(sys.argv[2])
 ax.plot(X[0:lim],L[0:lim],color="black")
except:
 ax.plot(X,L,color="black")
 

ax.set_yscale('log')
#ax.set_xlim(1,len(L)+1)
#ax.set_ylim(1,10e2)
try:
 thrs = int(sys.argv[3])
 ax.plot((thrs,thrs),(0,1000000),linestyle="--")
except:
 pass

#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels)

# NO LEGEND FOR YOU!!

canvas = FigureCanvasAgg(fig)
canvas.print_figure(myfile+".png", dpi=150)
#ax.savefig(args.OUTPUT_FILE[0]+".png")
