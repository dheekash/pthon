class person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print("Hello,my name is ", self.name)


p= person("Dheeraj")
p.say_hi()
