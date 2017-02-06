import glob
import random as rnd


def contract_edge(nodes,edges,n):
  edge = edges[n]
  node1 = edge[0]
  node2 = edge[1]
  for e in edges:
    if e[0] == node2:
      e[0] = node1
    if e[1] == node2:
      e[1] = node1
  removelist = []
  for e in edges:
    if e[0] == e[1]:
      removelist.append(e)
  for e in removelist:
    edges.remove(e)
  nodes.remove(node2)

#  print '---------------------------'
#  print node1,node2
  
def random_contract(nodes,edges):
  le = len(edges)
  ln = len(nodes)
  r = rnd.randint(0,le-1)
  while ln > 2:
#    print '   edges:',le,'  nodes:',ln
    contract_edge(nodes,edges,r)
    le = len(edges)
    ln = len(nodes)
    r = rnd.randint(0,le-1)




def get_nodes_edges(graph0):
  graph = list(graph0)

  nodes = []
  for n in graph:
    ni = n[0]
    node1 = [ni]
    nodes.append(node1)
  
  edges = []
  for n in graph:
    ni = n[0]
    node1 = nodes[ni-1]
    adjlist = n[1]
    for ni2 in adjlist:
      if ni2 > ni:
        n2 = graph[ni2-1]
        node2 = nodes[ni2-1]
        edges.append([node1,node2])

  return nodes,edges




if(__name__=='__main__'):
  files = glob.glob("*.txt")
  f = open(files[0])
  lines = f.readlines()
  f.close()

  graph0 = []
  for l in lines:
    a = [ int(s) for s in l.strip().split('    ')]
    node = (a[0],a[1:])
    graph0.append(node)


#  print nodes
#  print edges

  maxrun = 2000
  mincut = 10000000
  i=0
  while i < maxrun:
    nodes,edges = get_nodes_edges(graph0)
    print i, mincut
    random_contract(nodes,edges)
    if mincut > len(edges):
      mincut = len(edges)
    i+=1

  print mincut 
