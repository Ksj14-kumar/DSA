class A:
    """Operator overloading...."""
    def __init__(self,x=0,y=0) -> None:
        self.x= x 
        self.y= y
    def __str__(self) -> str:
        # print(f"{self.x+self.y}")
        return f"{self.x+self.y}"
    def __add__(self,value)->None:
        print(value)
        x= self.x+value.x
        y= self.y+value.y
        return f"this is addition {x,y}"

    def __sub__(self,value)->str:
        x= self.x-value.x
        y= self.y-value.y
        return f"this is substraction {x,y}"

    def __mul__(self,value)->str:
        x= self.x*value.x
        y= self.y*value.y
        return f"this is multiplication {x,y}"
    def __truediv__(self, value)->str:
        x= self.x/value.x
        y= self.y/value.y
        return f"this is divison {x,y}"
    def __mod__(self,value)->str:
        x,y=(self.x%value.x,self.y%value.y)
        return f"this is mode {x,y}"
p1= A(2,3)
print(p1)
p2= A(2,5)
print(p1+p2) # p1.__add__(p2)
print(p1-p2) # p1.__sub__(p2)
print(p1*p2)
print(p1/p2)
print(p1%p2)
# print(p1*p2)
# print(p1*p2)
