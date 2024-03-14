import sys
sys.stdin = open('input_10820.txt')
readl = sys.stdin.readline

# This is String(공백있을수도)'\n' [:-1]로 맨끝 '\n' 빼기 문자하나로 취급
# SPACE    1    SPACE
#  S a M p L e I n P u T     
# 0L1A2S3T4L5I6N7E8
#소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력
while True:
    line = readl()[:-1] #맨뒤에있는것만 빼라 '\'-1 #rstrip 제거 / 개행 '' 공백 둘다제거 -> rstrip
    if line == '':
        break
    # low = 0+1
    # upp = 0
    # num = 0
    # space = 0
    low, upp, num, space = 0, 0, 0, 0
    
    for ch in line:
        if ord('a') <= ord(ch) <= ord('z'):  # lower case
            low += 1
        elif ord('A') <= ord(ch) <= ord('Z'):  # upper case
            upp += 1
        elif ord('0') <= ord(ch) <= ord('9'):  # number
            num += 1
        else:
            space += 1
    
    print(low, upp, num, space)


# l = []
# s = []
# n = []
# s = []

# for i in line:  #This is String 
#     k = ord('i')-ord('a') 
#     if i < 0:   #ord('T')-ord('a') = 84 - 97 < 0
#         l.append(i)  #l = [T,A,,,,]
#     if i >= 0:    #ord('a')-ord('a') = 0
#         s.append(i)
#                        #SPACE    1    SPACE
        
        
     

