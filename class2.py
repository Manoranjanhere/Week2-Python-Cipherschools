def func(a,b,c):
    print(a)
    print(b)
    print(c)
#func(1,2,3)
def hello():
    print("Hello world :")
a = hello
a()
hello =2
print(hello)
a()
def func():
    print(1,2,3,4,sep=",")
func()
def func(a=1, b=2):
    print(a,b)
func()
func(2)
func(34,45)
def func(a,b,*c):
    print(a,b,c)
func(1,3,4,5,5,3,3,4,"Mano","sahoo")
def func(a,b,*c,d,e="Mano"):
    print(a,b,c,d,e)
func(55,6,566,"Mano",d="Sahoo")
def func(**c):
    print(c)
func(name="Mano")
print(sorted([3,5,8,1,28,7,5,2,24,5]))
add = lambda a,c:a+c
print(add(1,2))
a =5
c = print(a)
print(c)