import glob
import heapq 
#import numpy as np




if(__name__=="__main__"):
  files = glob.glob("*.txt")
  f = open(files[0])
  lines = f.readlines()
  f.close()
  
  nums = [ int(l) for l in lines ]
  
  ttbl = {}
  for n in nums:
    if not ttbl.has_key(n):
      ttbl[n]=1
    else:
      ttbl[n]+=1
  
  print "hash table bult!"

  numt = 0
  t = -10000
  while t <= 10000:
    print ' checking ', t
    for n in nums:
      if ttbl.has_key(t-n):
        numt+=1
        if (t-n)==n and ttbl[t-n]==1:
          numt-=1
        print ' yes ', t
        break
    t+=1
  
  print numt

  #427
