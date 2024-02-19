
import sys
sys.stdin = open('input_5789.txt')
readls = sys.stdin.readlines()

#여러줄 갖고옴
#한줄씩 비교
#가운데 두수비교
# [0,0,1,0,0,0,1,0]  index 0 부터 index 7까지,아스키코드 가운데 2개 8//2 = 4
# [0,0,1        ] 0 1 2 3번째랑, 4번째 절반나눠서 하나전이랑  3  4  7  7//2=3 몫, +1
# 수가 같으면 "한다"이고, 다르면 "안한다

for readl in readls[1:]: #한줄씩 비교
    readl = readline().rscript()
    if len(readl)//2 == len(readl)//2+1:
        print('Do-it')
    
    