class A:
    def __init__(self, a):
        self.a=a
    def __lt__(self,other):
        if (self.a>other.a):
            print("obj1 is > obj2")
        else:
            print("obj2 > obj1")
    def __eq__(self,other):
        if(self.a==other.a):
           return "both are equal"
        else:
            return "They are not equal"
obj1=A(3)
obj2=A(4)
print(obj1>obj2)
obj3=A(5)
obj4=A(5)
print(obj3==obj4)