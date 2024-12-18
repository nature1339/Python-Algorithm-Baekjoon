import sys
sys.stdin = open('input_5555.txt')
readl = sys.stdin.readline #readlines은 전부다 읽고끝남

find = readl().rstrip() #ABCD A,B,C,D
n = int(readl())
count = 0
print(f"find: {find}")
for _ in range(n):
    word = readl().rstrip() #ABCDXXXXXX
    print(f"{word} 검사 ---")
    word = word + word # [:len(find)-1] #2
    print(word)
    for i in range(10):
        print(f"{' ' * i}{word[i:i+len(find)]} <비교> {find}")
        if word[i:i+len(find)] == find:
            count += 1
            print("Find!!")
            break
    print("=" * 30)
print(count)
