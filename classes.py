class Studentt:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


student10 = Studentt('John', 'Eng', 3.6)
student20 = Studentt('Jane', 'CompSci', 3.8)
student30 = Studentt('Doe', 'Bio', 3.1)

print(student10.name)
print(student20.major)
print(student30.gpa)


print(student10.on_honour_roll())
print(student20.on_honour_roll())
print(student30.on_honour_roll())





