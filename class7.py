b = {1,2,3,4,5,7}#set
print(type(b))
for i in b:
    print(i)
a={1,2,7,8,6,5,6}
print(a-b)
print(a.union(b))
print(a.intersection(b))
a.add(85)
a.remove(5)
print(a)