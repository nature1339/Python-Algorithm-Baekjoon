k = ""  # i
l = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,  #j
     'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
     'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
     'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
     'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
     'z': 0}
# l.values()
# l['s']

# m=[english is a west germanic]
# language originating in england
# and is the first language for
# most people in the united
# kingdom the united states
# canada australia new zealand
# ireland and the anglophone
# caribbean it is used
# extensively as a second
# language and as an official
# language throughout the world
# especially in common wealth
# countries and in many
# international organizations
# l= 1 2 3 4 5  len(l)-1=4
#length 1 2 3 4 5
#index  0 1 2 3 4

count = 0

# list(l.keys()) [a, b, ]
# list(l.value()) [0,0,]
#  list(l.value())[j] =+ 1


def check(sentence):
    for j in range(len(sentence)-1):
        # if sentence[j] == list(l.keys())[i]:
        if sentence[j] != ' ':
            l[sentence[j]] += 1
    #         l.values()[i] += 1
    #             return False
    # return True    
                
                


k = str(input())
new_k = k.replace("\n","")
check(new_k) 
    
maxIdxes = []
for idx, value in enumerate(l.values()):
    if value == max(l.values()):
        maxIdxes.append(idx)
    
result = ""
for index in maxIdxes:
    result += list(l.keys())[index]

print(result)

# print(l.keys()[l.values().index(max(list(l.values())))])            
    