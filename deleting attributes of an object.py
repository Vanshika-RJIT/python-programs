class Point(object):
    x=0
    y=0
    def _init_(self,x,y):
        self.x=x
        self.y=y
p1=Point(4,5)
print((p1.x,p1.y))
del p1.y
print(p1.x)
print(p1.y)
