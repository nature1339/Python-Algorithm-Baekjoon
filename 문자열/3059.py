#입력줄의 수
#데이터입력 -> 입력줄만큼
# -> 리스트에서 0인거 찾기
# 빠진 알파벳 찾기
#-> 리스트에서 0인거 찾기 
# 그 알파벳의 아스크 코드 숫자 구하기
# -> 리스트에 넣기
# 더하기


n = int(input()) 
# m = input() #ABCDEFGHIJKLMNOPQRSTUVW
# n = input() #A
r = []
d = {}

for q in range(n):
    line = input().rstrip()
    # r.input() # ABCDEFGHIJKLMNOPQRSTUVW A
    # r.rstrip()  #ABCDEFGHIJKLMNOPQRSTUVWA
    
    d = {}
    for i in range(26):
        d[chr(ord('A') + i)] = False
        # {A:False B:False....} == itmes
        
    # for ch in range(len(r)): 0 ~ len(r)-1 # r.key() = 
    for ch in line:
        d[ch] = True

    s = 0
    for k, v in d.items():  # dictionary key, value
        if v == False:
            s += ord(k)
    print(s)


        
        
    



