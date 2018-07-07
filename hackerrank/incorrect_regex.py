# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()
for _ in range(n):
    try:
        re.compile(raw_input())
        print True
    except:
        print False 
