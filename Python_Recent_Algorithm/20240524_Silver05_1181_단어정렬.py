import sys
sys.stdin = open('input_1181.txt')



n = int(input())

arr = list(map(input() for i in range(n))) #arr = [but, i, wont...]
arr.sort()
print("\n".join(str,arr))




    
    