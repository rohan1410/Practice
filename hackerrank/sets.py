def average(array):
    # your code goes here
    s = set(array)
    su = 0
    for i in s:
        su += i
    return su/len(s)
