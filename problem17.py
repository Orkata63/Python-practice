#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = list()
    lowestScore = 100.00
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowestScore:
            lowestScore = score
        students.append([name,score])
    students=sorted(students, key=lambda x: x[1])
    students=[x for x in students if x[1] != lowestScore]
    printNum = students[0][1]
    students=sorted(students, key=lambda  x: x[0])
    for y in students:
        if y[1] == printNum:
            print(y[0])

