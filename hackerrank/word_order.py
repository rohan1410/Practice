# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

od = OrderedDict()
n = input()
for _ in range(n):
    c = raw_input()
    if c in od:
        od[c] += 1
    else:
        od[c] = 1
print (len(od))
for _ in od.values():
    print _,
