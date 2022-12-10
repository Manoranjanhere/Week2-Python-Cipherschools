a =[78,89,977,89]
print(a)
print(a[2])
print(a[-2])
a.insert(1,100)
print(a)
a.pop()
a.remove(100)
a.sort()
a.reverse()
print(a)
print([3747,74,848,94]+[464,83,847,84])
print(78 in a)
#sorted() this only retuns sorted value but dont change the value like sort(). 
#reversed() it also only return reverse list not cgange original list like reverse().also called lazy loading
print(list(map(lambda x:x**2,a)))
print(",".join(["jatin","samarth","molly"]))