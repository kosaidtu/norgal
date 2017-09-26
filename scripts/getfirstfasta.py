#!/usr/bin/env python

import sys
try:
 with open(sys.argv[1],"r") as fid:
  with open(sys.argv[2],"w") as fout:
   header = fid.readline()
   line = fid.readline()
   s = ""
   non = ""
   while line[0] != ">":
    s += line
    non = s.rstrip()
    line = fid.readline()
   fout.write(header.rstrip()+"_length_({0})\n".format(len(non)))
   fout.write(s)
except:
 print("Something went wrong with extracting the first contig..")
 sys.exit(1)
