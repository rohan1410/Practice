# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

def func(x):
    if x.isalpha():
        if x.isupper():
            return ord(x) - ord('A')
        else:
            return ord(x) - ord('a') - 26
    elif x.isdigit():
        if int(x) % 2 == 0:
            return 45 + int(x)
        else:
            return 30 + int(x)
    
    
s = raw_input()
ls = sorted(s,key = func)
for l in ls:
    print (l,end = '')
