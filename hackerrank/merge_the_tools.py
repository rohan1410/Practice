def merge_the_tools(string, k):
    # your code goes here
    ans = []
    for i in range(0,len(string),k):
        ans.append(string[i:i+k])
    for s in ans:
        a = ""
        for i in s:
            if i not in a:
                a += i
        print a
