#parent class
class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
    def address(self):
        print(self.name, self.contact)
#child class
class Docter(Person):
    pass
class Patient(Person):
    pass

doc1=Docter("Nish", 1234)
pat1=Patient("Anil", 5678)

doc1.address()
pat1.address()