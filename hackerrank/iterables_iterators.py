# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = input()
arr = raw_input().split()
k = input()

L = list(combinations(arr,k))
count = list(filter(lambda x: 'a' in x,L))
#print len(count),len(L),(1.0*len(count)/len(L))
print ("%.3f"%(1.0*len(count)/len(L)))
