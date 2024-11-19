import sys
sys.stdin = open('input_10984.txt')
readl = sys.stdin.readline

t = int(readl().rstrip()) #학기수 입력 2

# 3 4.3
# 2 2.0
# 4 0.0
# 2 4.0
for i in range(t): #2
    n = int(readl().rstrip()) #들었던 과목의 수 N
    total_c = 0
    total_g = 0
# 4
    for j in range(n): #4
        c, g = map(float,readl().split()) #학점 C와 성적 G가 , c=3  g=4.3
        total_c += c  #  total 학점  3+2+...
        total_g += c * g  #  total 성적  4.3+2.0...
        
    gpa = round(total_g/total_c, 1) #소수점
    print(int(total_c), gpa)

