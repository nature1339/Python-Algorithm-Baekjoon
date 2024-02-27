import sys
sys.stdin = open('input_1032.txt')
readl = sys.stdin.readline
# 3
# config.sys
# config.inf
# configures
n = int(readl()) 
out = list(readl().rstrip()) # [c,o,f...]
l = len(out) #전체길이 #파일 이름의 길이는 모두 같다.
for _ in range(n-1):#보통은 n인데 out에서 한번호출했기때문에 n-1, ## config.sys는 out에 받았으니, 셋째줄인 config.inf부터
    new = readl().rstrip() #두번째줄인 config.inf
    for i in range(l):
        if out[i] == '?':  #이미 ?이면 비교하지말고 넘어가자
            continue       #다음 for문실행
        if out[i] != new[i]: #두번째 줄이랑, 세번째줄 비교해서 틀리면 ,config.sys !=config.inf
            out[i] = '?' #다른부분 ? config.sys !=configures 비교해서 틀리면 ? 결론 config????상태
print("".join(out))  #join해서 "" 공백없이 출력, 만약 "-" c-o-n-f-i-g 

"""
ch_1 = [0]*26  #[1,3,1,0,...] figconsdf  [a, b, c, d] [1,3,1] abc=75 97+98+99 =150
ch_2 = [0]*26  #[1,3,1,2,...] configlll                            75  96 97 100         150
ch_3 = [0]*26  #[1,3,1,4,2,...]  configf2q3                        75           150

for i in range(n):  #config.sys
    for j in range(): # config.sys              
          ch_1[ord(j)-97] += 1
          #ch[ord(0)-97] = ch[ord(c)-97] = ch[99-97] = ch[2] +=1
          
         for i in ch_1:
          count += ch_1[i] 
          
          == ch_2 ==ch_3:
"""