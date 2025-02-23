s = {12,34,45,65,66,"ankesh"}
print(s,type(s))

s.add(222)
print(s,type(s))
s.remove(12)
print(s,type(s))

s={12,45,67,98,34}
s2={1,34,56,87}

print(s.union(s2))
print(s.intersection(s2))