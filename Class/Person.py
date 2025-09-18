class Person:
    idx = 1

    def __init__(self):
        print("Person is ruuning")
        self.idx = f"KOR{Person.idx:04}"
        Person.idx += 1

    def setName(self, name):
        if name != None and name.strip() != "":
            self.name = name
        else:
            self.name = "a"

    def getName(self):
        if "name" in dir(self):
            if self.name != None and self.name.strip() != "":
                return self.name
            else:
                return "Can not found the name"


class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student class is running")
        self.sidx = f"S-2025-{self.idx[-4:]:04}"

    def getSidx(self):
        return self.sidx


if __name__ == "__main__":
    tmp = Person()
    tmp.setName("gang")
    print(tmp.getName())
    print(tmp.name)

    gim = Student()
    gim.setName("Minji")
    print(f"Name : {gim.getName()} student id : {gim.sidx} id : {gim.idx}")
