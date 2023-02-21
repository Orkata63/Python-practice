#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
averageForStudent= (student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2])/3
print(format(averageForStudent, '.2f')) # using format. ( var, '  ' )