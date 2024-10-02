def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def fac(n):
    if n == 1:
        return 1
    # else:
    return n * fac(n-1)

# fac(4) -> 24
#     return 4 * fac(3) -> 4 * 6
#     fac(3) -> 6
#         return 3 * fac(2) -> 3 * 2
#         fac(2) -> 2
#             2 * fac(1) -> 2 * 1 
#             fac(1)
#             return 1
    

print(factorial(4))
print(fac(4))
print(factorial(10))
print(fac(10))