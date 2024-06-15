from collections import defaultdict
from collections import Counter
f = open("output.txt","w")
f.write("aBc")
f.close

f = open("output.txt", "r")
C = f.readlines()
D = []
F = defaultdict(int)
for i in C:
    if (i != i.lower()):
        i = i.lower()
    E = dict(Counter(i))
    D.append(E)
for j in D:
    for key, value in j.items():
        F[key] += value
F = dict(F)
print(F)

f.close()