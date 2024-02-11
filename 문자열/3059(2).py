# 한줄씩 받음 
# 알파벳에 없는애들 찾음-> 딕셔너리에 없는애들,
# 그 애들을 아스키코드로 변환후 
#합함

import sys
sys.stdin = open('input_3059.txt', 'r')
line = sys.stdin.readlines() # 모든 줄을 받음

d = {}  # 알파벳을 딕셔너리 만듬

for i in range(26): #2번째줄부터 한줄씩 반복 #key, value 
     d.value[i] == 0
     d.key[i] = chr(ord(65+i)) #chr(65)=A, B, C...
     #{'A': 0, 'B':0 ....}
     line = line.rstrip()  #1줄에서 rstrip
     if ch in d():  # 한줄을 반복해서 한문자ch가 d 딕셔너리에 있으면, value값을 1더함
         d.value =+ 1
     if d.value == 0:
         d.value += 1
         print(ord(d.key))    
         
    
    
    


