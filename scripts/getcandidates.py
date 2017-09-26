def getcandidates(mcoi):
 printcoi = "#Potential full/partial mitogenome candidates:\n#{0}\n#Scaffold:\tLength:\tHMM-score (COI):\n#{0}\n".format("-"*45)
 acoi = set()
 Lcoi = []
 dcoi = {}
 with open("ref/coihmm.tab") as fid:
  for line in fid:
   if line[0] == "#":
    continue
   ls = line.split()
   query = ls[2]
   score = float(ls[13])
   bias = float(ls[14])
   #print(query,score,bias)
   if query not in acoi:
    acoi.add(query)
    if score > bias:
     Lcoi.append(score)
     dcoi[query] = score
 
 if len(Lcoi) == 0:
  return [],printcoi
  
 dcoil = {}
 s = ""
 with open("assemblies/mtdna/scaffold.fa") as fid:
  h = fid.readline().rstrip()[1:]
  s = fid.readline().rstrip()
  for line in fid:
   if line[0] ==">":
    if len(s) > mcoi:
     dcoil[h] = s
     h = line.rstrip()[1:]
     s = ""
   else:
     s += line.rstrip()
  else:
   if len(s) > mcoi:
    dcoil[h] = s
 
 Lcoil = []
 for scaffold in dcoi:
  if scaffold in dcoil:
   if len(dcoil[scaffold]) > mcoi:
    Lcoil.append([scaffold,dcoi[scaffold],len(dcoil[scaffold])] )
 
 import operator
 Lcoil2 = sorted(Lcoil, key=operator.itemgetter(2), reverse=True)
 
 #Extract the contigs
 ccoi = 0
 for el in Lcoil2:
  ccoi += 1
  printcoi += "{0}\t{1}\t{2}\n".format( el[0],el[2],el[1]  )
  with open("candidate.{0}.length_{1}.fa".format(ccoi,el[2]),"w") as fout:
   fout.write("{0}_length_{1}\n{2}".format(el[0],el[2],  dcoil[el[0]] ))
 
 return Lcoil2, printcoi

if __name__ == "__main__":
  Lcoil2,printcoi = getcandidates()
  print(printcoi)
