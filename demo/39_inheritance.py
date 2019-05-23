class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname + ' ' + self.lastname)


# use the person class to create an object, then execute the printname method.

x = person("Jhon", "Doe")
x.printname()


class student(person):
    pass


x = student("Tom", "Jerry")
x.printname()
