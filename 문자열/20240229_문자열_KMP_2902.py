import sys
sys.stdin = open('input_2902'.txt)
readl = sys.stdin.readline

#Knuth-Morris-Pratt
words = readl().split('-') #Knuth Morris Pratt
first = [x[0] for x in words]
print(''.join(first))
