from collections import namedtuple

n, columns = int(input()), input().split()
Student = namedtuple('Student', columns)
print("{:.2f}".format(sum(int(Student._make(input().split()).MARKS) for _ in range(n)) / n))

