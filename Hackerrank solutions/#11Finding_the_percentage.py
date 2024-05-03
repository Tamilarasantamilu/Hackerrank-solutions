
 __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lst_marks = student_marks[query_name]
    percent = sum(lst_marks)/len(lst_marks)
    print('{p:1.2f}' .format(p = percent))
