# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,raw_input().split())
arr=map(int,raw_input().split(' '))
A=set(map(int,raw_input().split(' ')))
B=set(map(int,raw_input().split(' ')))
ans=0
'''
print arr
print A
print B
'''
for i in arr:
    if i in A:
        ans += 1
    if i in B:
        ans -= 1
print ans
