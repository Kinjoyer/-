class Test:
    def __init__(self, arr1, st):
        self.arr1 = arr1
        self.st = st
    def step(self):
        arrst = []
        for i in self.arr1:
            arrst.append(i**self.st)
        return arrst
class Test2(Test):
    def __init__(self, arr1, st):
        super().__init__(arr1, st)
    def sredn(self):
        return(sum(self.arr1)/len(self.arr1))
    def srednst(self):
        arr2 = Test.step(self)
        return(sum(arr2)/len(arr2))
sr = Test2([0, 1, 2], 3)
print(sr.step())
print(sr.sredn())
print(sr.srednst())

        
        