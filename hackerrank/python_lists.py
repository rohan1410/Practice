if __name__ == '__main__':
    N = int(raw_input())
    ans = []
    for _ in range(N):
        line = raw_input().split()
        if(line[0] == 'insert'):
            ans.insert(int(line[1]),int(line[2]))
        elif(line[0] == 'print'):
            print ans
        elif(line[0] == 'remove'):
            if(int(line[1]) in ans):
                ans.remove(int(line[1]))
        elif(line[0] == 'append'):
            ans.append(int(line[1]))
        elif(line[0] == 'sort'):
            ans.sort()
        elif(line[0] == 'reverse'):
            ans.reverse()
        elif(line[0] == 'pop'):
            ans.pop()
        #print ans
