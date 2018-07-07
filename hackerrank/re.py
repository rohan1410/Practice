# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = raw_input()
k = raw_input()
m = re.search(k,s)
i = 0
if not m:
    print (-1,-1)
while m:
    print (i + m.start(), i + m.end() - 1)
    s = s[m.start() + 1:]
    i += m.start() + 1
    m = re.search(k,s)
