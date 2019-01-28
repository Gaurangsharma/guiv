from itertools import permutations
n=list(str(input()))
l=list(permutations(n))
for i in l:
    print(*i)