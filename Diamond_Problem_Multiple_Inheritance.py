class a:
    def abd(self):
        print("class A")

class b(a):
    def abd(self):
        print("Class B")

class c(a):
    def abd(self):
        print("Class C")

class d(b,c):
    pass

calsd=d()
calsd.abd()
