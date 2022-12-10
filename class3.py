show = print
show("Hello World")
a = ["mano","jatin",1,1.5,"mansaj"]
for name in a:
    print(name)
a =9
b=4
temp =a+b
b = temp-b
a = temp-a
print("a=",a)
print("b=",b)
names = ["Mano","Anjan","jeeban","Ayush"]
scores=[50,22,32,21]
for i,name in enumerate(names):
    score = scores[i]
    print(name, "-",score)
for name,scores in zip(name,scores):
    print(name,"-",scores)