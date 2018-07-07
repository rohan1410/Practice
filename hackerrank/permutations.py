# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, k = raw_input().split()
k = int(k)
for i in list(permutations(sorted(s),k)):
    #print i
    print ''.join(i)
