# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k,m = map(int,raw_input().split())
arr = []
for _ in range(k):
    arr.append(list(map(int,raw_input().split()))[1:])
ans = map(lambda i: sum(x**2 for x in i)%m,product(*arr))
print max(ans)
