# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()
for _ in range(n):
    s = raw_input()
    print bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s))
    
