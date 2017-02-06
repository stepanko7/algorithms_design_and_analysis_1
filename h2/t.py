import glob


files = glob.glob("*.txt")
f = open(files[0])
lines = f.readlines()
f.close()
numarr = [int(s) for s in lines]
#numarr = [8,1,4,2,3,6,5,7]
#numarr = [3,1,4,2,8,6,5,7]
#numarr = [6,1,4,2,8,3,5,7]
#numarr = [1,2,3,4,5,6,7,8] #nc = 7+6+5+4+3+2+1=28
 
def partition_pivot(pi,a,si,ei):
  p = a[pi]

  t = a[pi] #swap pivot an 0 element
  a[pi] = a[si]
  a[si] = t

  i = si+1
  j = si+1
  while j < ei:
    if(a[j]<p):
      t = a[j]
      a[j] = a[i]
      a[i] = t
      i += 1
    j += 1
  
  t = a[si] #swap pivot at 0 and i-1 element
  a[si] = a[i-1]
  a[i-1] = t

  return i-1

def quick_sort(a,si,ei):
  num_comp = 0
  if(ei-si<2):
    return  num_comp

#  pi = si #problem 1      162085
#  pi = ei-1 #problem 2    164123
  
  p1 = a[si] #problem 3    138382
  p2 = a[si+(ei-si+1)/2-1]
  p3 = a[ei-1]
  if((p1<=p2 and p2<=p3)or(p3<=p2 and p2<=p1)): #p2 in the middle
    pi = si+(ei-si+1)/2-1
  if((p2<=p1 and p1<=p3)or(p3<=p1 and p1<=p2)): #p1 in the middle
    pi = si
  if((p2<=p3 and p3<=p1)or(p1<=p3 and p3<=p2)): #p3 in the middle
    pi = ei-1

#  print 'si,ei=',si,ei,'  a_before=', a[si:ei]
  num_comp += ei-si-1
  i = partition_pivot(pi,a,si,ei)
#  print 'i=',i, 'a_after=', a[si:ei], ' nc=',num_comp
#  print '===================='
  if(i>0):
#    print '1st call', a[si:i]
    num_comp += quick_sort(a,si,i)
  if(i+1<=ei):
#    print '2nd call', a[i+1:ei]
    num_comp += quick_sort(a,i+1,ei)
  return  num_comp
  

nc = quick_sort(numarr,0,len(numarr))
#print 'numarr=',numarr
print 'nc=',nc
