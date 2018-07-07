if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    mx = -200
    mx1 = -200
    for item in arr:
        if mx < item:
            mx1 = mx
            mx = item
        elif mx1 < item and mx != item:
            mx1 = item

    print mx1
