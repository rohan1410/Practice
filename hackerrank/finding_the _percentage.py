
def summation(scores):
    for item in scores:
        global s 
        s += item

if __name__ == '__main__':
    s = 0
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    summation(student_marks[query_name])
    print ('%.2f'%(s/len(student_marks[query_name])))
