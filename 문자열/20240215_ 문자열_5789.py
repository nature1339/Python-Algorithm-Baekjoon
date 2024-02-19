import sys
sys.stdin = open('input_5789.txt')
lines = sys.stdin.readlines()


for line in lines[1:]:
    line = line.rstrip()
    length = len(line)
    # 0 1 2 3 4 5 => length = 6
    #     2 3        
    # 0 1 2 ... n-1 | n n+1 ... 2n-1  => length = 2n
    #           n-1 | n
    # index: (length // 2) - 1, length // 2
    # line[length//2] 
    if line[length // 2 - 1] == line[length // 2]:
        print("Do-it")
    else:
        print("Do-it-Not")        
    


# # 함수 간단히 쓰기 위해서 
# readl = sys.stdin.readline

# 둘이 역할 같음
# a = input()
# a = sys.stdin.readline()
# a = readl()

# # 입력 전부를 한번에 받아옴
# a = sys.stdin.readlines()

#그 다음 문자열의 양 끝에서 수를 하나씩 고르고,
# 두 수를 비교한다. 수가 같으면 "한다"이고, 다르면 "안한다

# 반복문, 맨앞, 맨뒤 비교
# if 같으면 한다, 다르면 안한다.




