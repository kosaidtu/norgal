#!/usr/bin/env python

#scaffold_28	ref|NC_001675.1|	98.65	74	0	1	1	74	118929	119001	2e-27	130
#scaffold_35	ref|NC_001675.1|	100.00	54	0	0	5652	5705	3846	3793	1e-18	100
#scaffold_35	ref|NC_001675.1|	100.00	54	0	0	5652	5705	113671	113724	1e-18	100
#scaffold_35	ref|NC_025526.1|	96.23	53	1	1	5654	5705	3317	3265	4e-14	86.1
#scaffold_35	ref|NC_031664.1|	100.00	44	0	0	5662	5705	3450	3407	5e-13	82.4
#scaffold_35	ref|NC_031144.1|	100.00	44	0	0	5662	5705	111139	111096	5e-13	82.4
#scaffold_35	ref|NC_031144.1|	100.00	44	0	0	5662	5705	137412	137455	5e-13	82.4
#scaffold_35	ref|NC_029857.1|	100.00	44	0	0	5662	5705	124781	124824	5e-13	82.4
#scaffold_35	ref|NC_031656.1|	100.00	43	0	0	5663	5705	3458	3416	2e-12	80.5
#scaffold_35	ref|NC_025528.1|	92.98	57	1	3	5652	5705	123749	123693	2e-12	80.5

import sys,json
import operator
from shutil import copyfile

def main(f1,spath,b):
# printcoi = "#Potential full/partial mito/plastid genome candidates:\n#{0}\n#Type\tScaffold:\tIdentity:\tBit-score:\tmtRNA-genes\tBest-hit reference:\n#{0}\n".format("-"*45)
 printcoi = "#Potential full/partial mito/plastid genome candidates:\n#{0}\n#Type\tScaffold:\tIdentity:\tBit-score:\tBest-hit reference:\n#{0}\n".format("-"*45)

 dcoil = {}
 s = ""
 with open("assemblies/mtdna/scaffold.fa") as fid:
  h = fid.readline().rstrip()[1:]
  s = fid.readline().rstrip()
  for line in fid:
   if line[0] ==">":
    dcoil[h] = s
    h = line.rstrip()[1:]
    s = ""
   else:
     s += line.rstrip()
  else:
   dcoil[h] = s

 m = json.load( open(spath+"/blast/mito.json") )
 p = json.load( open(spath+"/blast/plastid.json") )
 with open(f1) as fid:
  L = []
  unique = set()
  for line in fid:
   ls = line.rstrip().split()
   contig = ls[0]
   ref = ls[1]
   if ref in unique:
    continue
   unique.add(ref)
   perc = float(ls[2])
   alen = int(ls[3])
   Eval = float(ls[-2])
   score = float(ls[-1])
   if ref in m:
    Type = "m"
    name = ":".join(m[ref].split(":")[0:-1])
    slen = m[ref].split(":")[-1]
   elif ref in p:
    Type = "p"
    name = ":".join(p[ref].split(":")[0:-1])
    slen = p[ref].split(":")[-1]
   else:
    Type = "u"
    name = ref
    slen = "?"
   contigL = "{0}:{1} bp".format(contig,len(dcoil[contig]))
   L.append( [ Type,contigL,perc,alen,slen,Eval,score,name  ]  )

 if len(L) < 1:
  return "","",""
 Lsort = sorted(L, key=operator.itemgetter(6), reverse=True)
#Comment out next 4 lines for mtRNA version
 with open("blast.report","w") as fout:
  fout.write(printcoi)
  for i in Lsort[0:b]:
   fout.write("{0}\n".format("\t".join(   [str(x) for x  in i]  )    )  )

 #Extract the contigs
 for el in Lsort[0:b]:
  with open("candidates/{0}.fna".format( el[1].split(":")[0]  ),"w") as fout:
   fout.write(">{0}_length_{1}bp\n{2}\n".format(  el[1].split(":")[0], el[1].split(":")[1].split()[0]  ,  dcoil[el[1].split(":")[0]]  ))

 copyfile("candidates/{0}.fna".format( Lsort[0][1].split(":")[0]  ), "candidate.fna"  )

 return "candidate.fna",Lsort,printcoi

if __name__ == "__main__":
 main(sys.argv[1],sys.argv[2],int(sys.argv[3]))
#res.m8   path-to-json_files   number of hits to report


