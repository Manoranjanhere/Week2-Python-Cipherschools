student1 ={"name": "Mano"
        "marks: 100"}#Abstraction
class person:
        pass
p=person()#object
print(p)
class person:
        name ="Mano"
        def say_hi(self):
                print(f"Hello Everyone! I am {self.name}")
p=person()
p.say_hi()
person.say_hi(p)