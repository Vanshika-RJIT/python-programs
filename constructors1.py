class Addition:
    a=0
    b=0
    c=0
    def _init_(self,x,y):
        self.a=x
        self.b=y
        self.c=self.a+self.b
    def show(self):
        print(self.a,"+",self.b,"=",self.c)
o=Addition(12,3)
o.show()
print(o)
del o
print(o)
