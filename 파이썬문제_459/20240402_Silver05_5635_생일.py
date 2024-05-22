import sys
sys.stdin = open('input_5635.txt')
readl = sys.stdin.readline


n = int(readl()) #Mickey 1 10 1991

students = []
for i in range(n):
    name, dd, mm, yyyy = readl().split() #Mickey 1 10 1991
    dd, mm, yyyy = map(int, [dd, mm, yyyy]) # list는 값을 바꾸려할때
    # [('Mickey', (1991, 10, 1)), ('Alice', (1990, 12, 30)), ...]
    #  
    students.append((name, (yyyy, mm, dd))) #()는 tuple, 값못바꿀때

students.sort(key=lambda x:x[1]) #x= ('Mickey', (1991, 10, 1))
#lambda x를 넣으면 x[1]을 리턴, 이름없는 함수 = lambda, tuple은 (1991, 10, 1)를 알아서 오름차순으로 sort (내림차순은 reverse = True)
# def f(x):
#     return x[1]
# for st in students:
#     print(st)
print(students[-1][0]) #''은 저절로 없이 출력됨 'Tom'-> Tom
print(students[0][0])

# temp_dd, temp_mm, temp_yyyy = 0,0,0
# age = []

# for i in range(n):
#     name, dd, mm, yyyy = map(readl().split()) #Mickey 1 10 1991
#     dd, mm, yyyy = map(int, [dd, mm, yyyy ])   #'dd' ->문자
        
#     if temp_yyyy > yyyy:
#         temp_yyyy = yyyy
#         age.append(yyyy)
#     if temp_mm > mm:
#         temp_mm = mm
#         age.append(mm)
#     if temp_dd > dd:
#         temp_dd = dd
#         age.append(dd)
# print(age[0,1])        
    