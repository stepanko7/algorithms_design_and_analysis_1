import glob
import heapq as hp
#import numpy as np




if(__name__=="__main__"):
  files = glob.glob("*.txt")
  f = open(files[0])
  lines = f.readlines()
  f.close()
  
  nums = [ int(l) for l in lines ]
  
  lowesthigh = []
  highestlow = []
  
#  n0 = nums[0]
#  n1 = nums[1]
#  nums.remove(n0)
#  nums.remove(n1)
#  
  
  summed = 0
  for n in nums:
    maxmin = 10**100
    lenhl = len(highestlow)
    if(lenhl>0):
      maxmin = -highestlow[0]

    minmax = -10**100
    lenlh = len(lowesthigh)
    if(lenlh>0):
      minmax = lowesthigh[0]
    
    hp.heappush(highestlow,-n)

    lenhl = len(highestlow)
    lenlh = len(lowesthigh)
    if(lenhl-lenlh > 1):
      t = -hp.heappop(highestlow)
      hp.heappush(lowesthigh,t)

    if(lenhl>0):
      maxmin = -highestlow[0]
    if(lenlh>0):
      minmax = lowesthigh[0]

    if(minmax<maxmin and (lenlh>0 and lenhl>0)):
      t = -hp.heappop(highestlow)
      t2 = hp.heappop(lowesthigh)
      hp.heappush(lowesthigh,t)
      hp.heappush(highestlow,-t2)

    summed += -highestlow[0]

#    print 'n:',n
#    print 'highestlow:',highestlow
#    print 'lowesthigh:',lowesthigh
#    print 'median:',-highestlow[0]
#    print '-----------------------'
  
  print summed%10000


  #65443528
