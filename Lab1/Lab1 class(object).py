#Person : has first name, last name, age

class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def changeName(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def haveBirthday (self):
        self.age += 1

    def __str__(self):
        return self.firstname + " " + self.lastname + " is " + str(self.age) + " years old."

Jaeha = Person("Jaeha", "Huh", 22)
print(Jaeha)
