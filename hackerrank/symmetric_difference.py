# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(raw_input())
arr = set(map(int,raw_input().split()))
n = int(raw_input())
arr1 = set(map(int,raw_input().split()))
ans = sorted(arr.difference(arr1))
ans1 = sorted(arr1.difference(arr))
ans2 = ans + ans1
for item in sorted(ans2):
    print item
