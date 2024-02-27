import sys
sys.stdin = open('input_2711.txt')
readls = sys.stdin.readlines()
# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON
#4, "MISSPELL", 1, PROGRAMMING
# input(), readline(), readlines()
for line in readls[1:]:
    x, line = line.split()  # rstrip
    x = int(x)
    print(line[:x-1] + line[x:])
    # line[i]= line.remove(i)
    # print(line)
#     >>> 
# >>> a = 'abc.def.xyz'
# >>> 
# >>> 
# >>> a.split('.')
# ['abc', 'def', 'xyz']
# >>>
# >>> 
# >>> a = 'abc def xyz' 
# >>> 
# >>> a.split(' ')
# ['abc', 'def', 'xyz']
# >>>
 