import sys

sys.stdin = open("input_1254.txt")
readl = sys.stdin.readline


word = readl().rstrip()
n = len(word)


def isPel(string):
    return string == string[::-1]


ans = n  # 입력길이
for i in range(n):
    if isPel(word[i:]):  # -> 중간에 word[i:]가 펠린드롬인지확인
        # 펠린드롬이면 전체글이 펠린드롬되게 i앞에거를 더해서 전체가 펠린드롬되게함
        ans += i  # 추가할개수 -> 목표가 펠린드롬의 갯수
        break
print(ans)

# ans <- 4(abab) + 1(a) + 3(aba)
# abab
# 처음 펠린드롬 만족하면 break
