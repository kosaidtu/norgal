#!/usr/bin/env python

import sys
import numpy as np

def getpercentile(coveragefile):
 with open(coveragefile) as fid:
  L = []
  l = 0
  for el in fid:
   if l > 100000:
    break
   depth = int(float(el.split()[-1]))
   if depth > 0:
    L.append(depth)
    l += 1

 upper = int( 0.75*len(L)-1    )
 lower = int( 0.25*len(L)-1    )
 L = sorted(L)[lower:upper]
 return (  int(5*np.mean(L))    )

 #print("mean: {0}".format(    int(5*round(np.mean(L)))          ) )
 #print("mediam: {0}".format(  int(5*round(np.median(L)))        ) )
 #print("mean/median: {0}".format(  int(5*(np.mean(L)+np.median(L))/2  )            ) )

# percentile = 0.998 #99.8 % of genomic reads discarded
# return sorted(L)[round( percentile*len(L)-1    )]
# return (int(5*(np.mean(L)+np.median(L))/2  ))
# return (int(5*round(np.median(L))  ))
# return (int(5*round(np.mean(L))  ))
# return (int(np.percentile(L,99.8)))

if __name__ == "__main__":
 print(getpercentile(sys.argv[1]))
