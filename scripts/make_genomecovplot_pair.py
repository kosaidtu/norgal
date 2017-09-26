#!/usr/bin/env python

from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from matplotlib.backends.backend_agg import FigureCanvasAgg
#import matplotlib.numerix as nx


import matplotlib
#matplotlib.use('Agg')
from argparse import ArgumentParser

parser = ArgumentParser(description="Use 'bedtools genomecov -d' to get a genomecov file from a bam alignment.")
parser.add_argument('BAM_COV_FILE', help="mitochondrial coverage file", nargs=1)
parser.add_argument('BAM_COV_FILE2', help="genomic coverage file",nargs=1)
parser.add_argument('CUTOFF', help="Cut-off used for binning",type=int,nargs=1)
parser.add_argument('OUTPUT_FILE', help="Name of output plot",nargs=1)
parser.add_argument("-s", type=int, default=0,
                    help="Start pos (0)")
parser.add_argument("-e", type=int, default=100000,
                    help="End pos (100000)")
args = parser.parse_args()

i = 0
with open(args.BAM_COV_FILE[0], "r") as fid:
 with open(args.BAM_COV_FILE2[0], "r") as f2:
  L = []
  for line in fid:
   i+=1
   if i > args.s:
    L.append(int(float(line.split()[-1].rstrip())))
   if i==args.e:
    break
  L2 = []
  k = 0
  for line in f2:
   k += 1
   if k <= i:
    L2.append(int(float(line.split()[-1].rstrip())))
   else:
    break

fig = Figure()
ax = fig.add_subplot(111)
ax.set_title("Reads mapped to assembly")
ax.set_xlabel( "Genome position")
ax.set_ylabel( "Depth")
#ax.bar(range(1,len(L)+1),L,log=True)
#ax.plot(range(1,len(L2)+1),L2,log=True,color="red",linestyle="--")

#ax.bar(range(1,len(L2)+1),L2,zorder=2,color='blue')
#ax.bar(range(1,len(L)+1),L,zorder=1,color="green")
#plot1 = ax.plot([0,len(L)+1],[args.CUTOFF[0],args.CUTOFF[0]],zorder=3,linewidth=3,color="r",linestyle="--")
X = range(1,len(L2)+1)
X2 = range(1,len(L)+1)
####print(len(X),len(L2),len(L))

#ax.plot(X,L2,zorder=2,color="green")
#ax.fill_between(X,0,L2,zorder=2,color="#fdb863",alpha=1,edgecolor="none")

#ax.plot(X,L,zorder=1,color="blue")
#ax.fill_between(X,0,L,zorder=1,color="#b2abd2",alpha=1,edgecolor="none")

#ax.fill_between(X,0,L2,zorder=2,color="#525252",alpha=1,label="Genomic DNA")
#ax.fill_between(X,0,L,zorder=1,color="#969696",alpha=1,label="mtDNA")
#ax.plot([0,len(L)+1],[args.CUTOFF[0],args.CUTOFF[0]],zorder=3,linewidth=3,color="#cccccc",linestyle="--",label="Cut-off")
#ax.set_yscale('log')
#ax.set_xlim(1,len(L2)+1)

#ax.fill_between(X,0,L2,zorder=2,color="#525252",alpha=1,label="Genomic DNA")
#ax.fill_between(X,0,L,zorder=1,color="#969696",alpha=1,label="mtDNA")
#ax.plot([0,len(L)+1],[args.CUTOFF[0],args.CUTOFF[0]],zorder=3,linewidth=3,color="#cccccc",linestyle="--",label="Cut-off")
#ax.set_yscale('log')
#ax.set_xlim(1,len(L2)+1)


ax.fill_between(X,0,L2,zorder=2,color="#969696",alpha=1,label="Genomic DNA")
ax.fill_between(X2,0,L,zorder=1,color="#cccccc",alpha=1,label="mtDNA")
ax.plot([0,len(L)+1],[args.CUTOFF[0],args.CUTOFF[0]],zorder=3,linewidth=3,color="black",linestyle="--",label="Cut-off")
ax.set_yscale('log')
ax.set_xlim(1,len(L)+1)



#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels)

# NO LEGEND FOR YOU!!

canvas = FigureCanvasAgg(fig)
canvas.print_figure(args.OUTPUT_FILE[0]+".png", dpi=300)
#ax.savefig(args.OUTPUT_FILE[0]+".png")
