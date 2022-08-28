class Computer:

    def __init__(self):
        self.name = "Giri"
        self.age = 44

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are Same")
else:
    print("They are Different")

c1.name = "Kireeti"

print(c1.name)

print(c2.name)
print(c2.age)