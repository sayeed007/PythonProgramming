from collections import namedtuple

N = int( input() )
students = namedtuple('student', input())

total_marks = 0

for i in range(N):
    lis = list( input().split() )
    student = students(lis[0], lis[1], lis[2], lis[3])
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / N))



