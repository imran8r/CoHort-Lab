class rectangle :
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print('The area is:',self.l*self.b)
l=float(input('lenght?'))
b=float(input('width?'))
v=rectangle(l,b)
v.area()
        
