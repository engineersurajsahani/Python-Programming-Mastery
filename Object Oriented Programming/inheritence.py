class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(A):
    def display(self):
        print("Class C")

class D(C,B):
    # def display(self):
    #     print("Class D")
    pass

a=A()
b=B()
c=C()
d=D()

a.display()
b.display()
c.display()
d.display()