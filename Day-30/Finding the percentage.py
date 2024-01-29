if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    # Reading student records
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()

    # Calculate and print the average marks for the specified student
    if query_name in student_marks:
        average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
        print("{:.2f}".format(average_marks))
    else:
        print("Student not found.")
