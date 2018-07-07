def minion_game(string):
    cnt = 0
    cnt1 = 0
    vowel = 'AEIOU'
    for i in range(len(string)):
        if(string[i] in vowel):
            cnt += len(string) - i
        else:
            cnt1 += len(string) - i
    if(cnt < cnt1):
        print "Stuart", cnt1
    elif(cnt1 < cnt):
        print "Kevin", cnt
    else:
        print "Draw"
