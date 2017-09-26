#!/usr/bin/env python

from __future__ import print_function
import sys

with open(sys.argv[1]) as fid:
 full = ""
 header = fid.readline()
 full = fid.readline().rstrip()
 line = fid.readline().rstrip()
 while line:
  full += line
  line = fid.readline().rstrip()
 head = full[0:1000]

kmax = int(len(full)/2)
head = full[0:kmax]
print(kmax)

if kmax > 8:
 k = 8
elif kmax > 2:
 k = 2
else:
 k = 1

#k=8
newk = 0
#while k<1000:
while k<kmax:
 k+=1
 start = head[0:k]
 end = full[-k:]
 if start == end:
  newk = k

if newk != 0:
 k = newk
 print("k= {2}, possible match!:\n{0}\n{1}".format(  head[0:k], full[-k:]  ,   k))
 print("Found and trimmed {0} overlaps at the ends!".format(k))
 print("Warning! Could be repeats. Do a dot plot for the non-trimmed fasta-files")
 print("and run more thourough circularization software to be sure!")
 newseq = full[0:-k-1]
 with open("circular.fa","w") as fout:
  fout.write(">rotated_mtDNA_candidate_length({0})_circular_overlaps({1})\n{2}".format(len(newseq),k,newseq))
else:
 with open("circular.fa","w") as fout:
  fout.write(">rotated_mtDNA_candidate_length({0})_no_circular_overlaps\n{1}".format(len(full),full))
 print("Could not find repeated regions for the last {0} nucleotides! => non-circular? Bad-assembly?".format(k))
 print("I suggest you try to run priceTI assembler on your current mtDNA and spike it with your reads")


