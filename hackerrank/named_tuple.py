# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
fields = raw_input().split()

total = 0
for i in range(N):
    students = namedtuple('student',fields)
    field1, field2, field3,field4 = raw_input().split()
    student = students(field1,field2,field3,field4)
    total += int(student.MARKS)
#print total,N
print('{:.2f}'.format(1.0*total/N))
