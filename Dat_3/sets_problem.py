a={14,43,24,13,14,35,45}
max=max(a)
min=min(a)
print("Min of the set a",min)
print("Max of the set a",max)
a=[14,43,24,13,14,35,45]
b=[14,24,13,24,31]
c=[24,13,34,13,14]
print("common in all sets",set(a)&set(b)&set(c))
a={14,43,24,13,14,35,45}
b={14,24,13,24,31}
print(a.difference(b))
a.discard(14)
print(a)