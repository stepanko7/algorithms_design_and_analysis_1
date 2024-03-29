import glob
import heapq 
#import numpy as np

class Node:
  def __init__(self,n):
    self.num = n
    self.outedges = []
#    self.inedges = []
    self.explored = False
    self.f = -1



#print edges[0]

def DFSnorec(node,lead,t,numexpl,reverse=False):
  stack = []  
  node.explored = True
  numexpl[0] += 1

  if(not reverse):
    i = 0
    while True:
      if(i>=len(node.outedges)):
        t[0] += 1
        node.f = t[0]
        if len(stack) > 0:
          node,i = stack.pop()
          i += 1
          continue
        else:
          break
      if(not node.outedges[i][1].explored):
        stack.append([node,i])
        node = node.outedges[i][1]
        node.explored = True
        numexpl[0] += 1
        i = 0
      else:
        i += 1
  else:
    i = 0
    while True:
      if(i>=len(node.inedges)):
        t[0] += 1
        node.f = t[0]
        if len(stack) > 0:
          node,i = stack.pop()
          i += 1
          continue
        else:
          break
      if(not node.inedges[i][0].explored):
        stack.append([node,i])
        node = node.inedges[i][0]
        node.explored = True
        numexpl[0] += 1
        i = 0
      else:
        i += 1


def DFS(node,lead,t,numexpl,reverse=False):
  node.explored = True
  numexpl[0] += 1
  if(not reverse):
    for e in node.outedges:
      if not e[1].explored:
        DFS(e[1],lead,t,numexpl,reverse)
  else:
    for e in node.inedges:
      if not e[0].explored:
        DFS(e[0],lead,t,numexpl,reverse)
  t[0] += 1
  node.f = t[0]




def compute_SCCs(nodes):
  nodes.reverse()
  t = [0]
  for n in nodes:
    if not n.explored:
      numexpl = [0]
      DFSnorec(n,n,t,numexpl,True)
#      DFS(n,n,t,numexpl,True)
#      print '1 numexpl[0], t[0]:',numexpl[0], t[0]

  
  def cmpf(n1,n2):
    if(n1.f > n2.f):
      return -1
    else:
      return 1

  nodes.sort(cmp=cmpf)

  for n in nodes:
    n.explored = False
  
  SSClist = []
  for n in nodes:
    if not n.explored:
      numexpl = [0]
      DFSnorec(n,n,t,numexpl)
#      DFS(n,n,t,numexpl)
      SSClist.append(numexpl[0])
#      print '2 numexpl[0], t[0]:',numexpl[0], t[0]

  return SSClist




def Dijkstra(nodes,nodeS):
  v = list(nodes)
  x = []
  heap = []

  nodeS.f = 0
  for e in nodeS.outedges:
    heapq.heappush(heap,(e[2]+nodeS.f,e[1],e))
  x.append(nodeS)

  while len(x)<len(v):
    fW,nodeW,nodeV = heapq.heappop(heap)
    if not nodeW in x:
      nodeW.f = fW
      for e in nodeW.outedges:
        heapq.heappush(heap,(e[2]+nodeW.f,e[1],e))
      x.append(nodeW)

#    dellist = []
#    for n in heap:
#      if nodeW==n[1] and nodeV==n[2]:
#        dellist.append(n)
#    for n in dellist:
#      heapq.heappop(n)

  return nodes 





if(__name__=="__main__"):
  files = glob.glob("*.txt")
  f = open(files[0])
  lines = f.readlines()
  f.close()
  
  maxnum = 0
  edges = []
  for l in lines:
    nums = l.strip().split(' ')
    num0 = int(nums[0])
    if(num0>maxnum):
      maxnum = num0
    for s in nums[1:]:
      s1,s2 = s.strip().split(',')
      numX = int(s1)
      lenX = int(s2)
      edges.append((num0,numX,lenX))

  print "edge list done"

  nums = range(1,maxnum+1)
  nodes = []
  for n in nums:
    nodes.append(Node(n))
  del nums
  del lines


  print "node list done"

  for e in edges:
    n1 = e[0]
    n2 = e[1]
    ln = e[2]
    edge = (nodes[n1-1],nodes[n2-1],ln)
    nodes[n1-1].outedges.append(edge)
#    nodes[n2-1].inedges.append(edge)

  print "out in edges done list done"
  
  print "len(nodes):",len(nodes)
  print "len(edges):",len(edges)

  Dijkstra(nodes,nodes[0])
  numlist = [7,37,59,82,99,115,133,165,188,197]
  answer = [str(nodes[i-1].f) for i in numlist]
  print "answer:",','.join(answer)
  

#  sscs = compute_SCCs(nodes)
#  sscs.sort()
#  sscs.reverse()
#  print "sscs=",sscs[0:5]

