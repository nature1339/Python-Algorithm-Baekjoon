import sys
sys.stdin = open('input_1357.txt')
readl = sys.stdin.readline

X, Y = readl().split()
# Rev(X), Rev(Y) = 1, 1
# Rev(X) = X[::-1]
# Rev(Y) = Y[::-1]

def Rev(X):  #123
    X= X[::-1] #321  
    return(X)
def Rev(Y): #100
    Y= Y[::-1] #001 
    return(Y)

print(Rev(int(Rev(X))+int(Rev(Y))))