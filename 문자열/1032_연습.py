import sys
sys.stdin = open('input_1032.txt')
readl = sys.stdin.readline

# config.sys = c, o, n, ...    99, ..
# config.inf = c, o, n, ...    99,, 
# configures
# 첫번째 호출 -> out 변수에
# 
n = int(readl())
out = list(readl().rstrip)  # config.sys 처음거가 기준이고, 두번째거를 비교하고, 세번째도 비교 [c, o, n, ...] 
            #[c, o, n, ...]
# 3
# config.sys
# config.inf
# configures
l = len(out)
for _ in range(n-1): #첫번째줄은 out으로 해서 두번째부터
    for i in range(l):
        new = readl().rstrip #2번째 = new에 담고
        if out[i] == '?': #out의 i와 new의 i와 같으면 반복문 다시돌기
            continue
        if out[i] != new[i]:
            out[i] == '?'
print("".join(out))              
        