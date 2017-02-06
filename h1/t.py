import glob


files = glob.glob("*.txt")
f = open(files[0])
lines = f.readlines()
f.close()
numarr = [int(s) for s in lines]
#numarr = [8,1,4,2,3,6,5,7]

def merge_sort_inv_count(a):
  n = len(a)
#  if(n==2):
#    if(a[0]<=a[1]):
#      return a,0
#    else:
#      return [a[1],a[0]],1 
#  elif(n==1):
#    return a,0
  if(n==1):
    return a,0
  a1 = a[:n/2]
  a2 = a[n/2:]
  n1 = len(a1)
  n2 = len(a2)

#  print 'a:', a


  a1, ninv1 = merge_sort_inv_count(a1)
  a2, ninv2 = merge_sort_inv_count(a2)
#  print 'a1:', a1
#  print 'a2:', a2
  
  ninv = ninv1 + ninv2
  i=0
  j=0
  ao = []
  k = 0
  while k < n:
#    print 'n1,n2,i,j',n1,n2,i,j
    if((j>=n2) or (i<n1 and a1[i]<a2[j])):
      ao.append(a1[i])
      i += 1
    else:
      ao.append(a2[j])
      j += 1
      ninv += n1 - i
    k += 1
#    print 'ao:', ao

  return ao, ninv 


a,ninv = merge_sort_inv_count(numarr)
print ninv
