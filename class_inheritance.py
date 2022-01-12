class a:
    def display(self):
        print("Class A read.")
class b(a):
    def show(self):
        print("Class B read.")

d = b()
d.show()
d.display()
