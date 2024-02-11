

import sys
sys.stdin = open('input_4458.txt', 'r') 
lines = sys.stdin.readlines()



for line in lines[1:]:  #p,o,w,d,e,... #첫라인은 줄수라서
    line = line.rstrip()
    if ord(line[0]) >= 65+32:    #  ord('a'+0), ord(65+0), 65+32, 65+1+32, a
    #{a:0, b:0,}     첫글자가 소문자일경우        
        print(chr(ord(line[0])-32), end="")
        print(line[1:]) #이미 첫글자를 대문자로 바꿔서 프린트를 앞에서 해서 두번째부터 print
    else:          #첫글자가 대문자일경우
        print(line)    
    
