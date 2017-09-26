#!/usr/bin/env python

from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from matplotlib.backends.backend_agg import FigureCanvasAgg
#import matplotlib.numerix as nx


import matplotlib
#matplotlib.use('Agg')
from argparse import ArgumentParser

parser = ArgumentParser(description="Use 'bedtools genomecov -d -ibam <bam-file>' to get a genomecov file from a bam alignment.")
parser.add_argument('BAM_COV_FILE', nargs=1)
parser.add_argument('OUTPUT_FILE', nargs=1)
parser.add_argument("-s", type=int, default=0,
                    help="Start pos (0)")
parser.add_argument("-e", type=int, default=100000,
                    help="End pos (100000)")
args = parser.parse_args()

i = 0
with open(args.BAM_COV_FILE[0], "r") as fid:
 L = []
 for line in fid:
  i+=1
  if i > args.s:
   L.append(int(float(line.split()[-1].rstrip())))
  if i==args.e:
   break

print("DONE PARSING!")
fig = Figure()

ax = fig.add_subplot(111)

X = range(1,len(L)+1)
ax.fill_between(X,0,L,zorder=1,color="#cccccc",alpha=1,label="mtDNA")
ax.set_yscale('log')
ax.set_xlim(1,len(L)+1)

ax.set_title("Reads mapped to assembly")
ax.set_xlabel( "Genome position")
ax.set_ylabel( "Depth")
canvas = FigureCanvasAgg(fig)
canvas.print_figure(args.OUTPUT_FILE[0]+".png", dpi=80)
#ax.savefig(args.OUTPUT_FILE[0]+".png")
