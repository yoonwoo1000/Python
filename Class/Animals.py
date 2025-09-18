class Cat:
    def __init__(self):
        print("Cat() is running")
        self.name = ""
        self.birth = "2025"
        self.type = ""

    def printInfo(self):
        print(f"cat name :  {self.name}")
        print(f"cat birth:  {2025 - int(self.birth)}")
        print(f"cat type :  {self.type}")


class Puppy:
    def __init__(self):
        print("Puppy() is running")
        self.name = ""
        self.birth = "2025"
        self.type = ""
        self.idx = 0

    def printInfo(self):
        print(f"Puppy name :  {self.name}")
        print(f"Puppy birth:  {2025 - int(self.birth)}")
        print(f"Puppy type :  {self.type}")
        print(f"Puppy idx :  {self.idx}")
