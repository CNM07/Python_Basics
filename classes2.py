class Student:

    name = ""
    age = 0
    gender = ""
    math = 0
    eng = 0
    swa = 0
    sci = 0
    soc = 0
    total = 0
    avg = 0

    def __init__(self, name, age, gender, math, eng, swa, sci, soc,):
        self.name = name
        self.age = age
        self.gender = gender
        self.math = math
        self.eng = eng
        self.swa = swa
        self.sci = sci
        self.soc = soc
        self.total()
        self.avg()

    def sum(self):
        return 23 + 45

    def total(self):
        self.total = self.math + self.eng + self.swa + self.sci + self.soc
        return self.total

    def avg(self):
        self.avg = self.total/5
        return self.avg




class Foo:
    def __init__(self, v):
        self.v = v
    def printVal(self):
        print(self.v)


obj1 = Foo(1)
obj2 = Foo('string')

obj1.printVal()
obj2.printVal()





