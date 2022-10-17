
class A:
    a="this is a"
    b= "this is b"
    number=90
    def __init__(self) -> None:
        print("calling....")


    def sum(self,value):
        self.init= 0
        for i in range(0,value):
            self.init +=i
        return self.init;

    def add(self, a,b):
        return a+b


    def sub(self,a,b):
        return a-b

    def Multi(self,a,b):
        return a*b


obj1= A()
print(obj1.a)
print(obj1.b)
print(obj1.number)
print(obj1.sum(25))
print(obj1.add(2,5))
print(obj1.Multi(5,2))
print(obj1.sub(5,6))



class B(A):


    def __init__(self) -> None:
        super().__init__()
        self.__price=60
    def Add(self, name):
        return name

    def getter(self):
        print(self.__price)
        # return self._price

    def set(self, price):
        self._price= price


obj2= B()
print(obj2.add(5,6))
obj2.getter()
obj2.__price=8000
obj2.set(5600)
obj2.getter()


class Parrot:
    def __init__(self) -> None:
        pass
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")
class Penguin:
    def __init__(self) -> None:
        pass
    def fly(self):
        print("parrot can't fly")
    def swim(self):
        print("parrot can swim")



# abstraction
def Called(call):
    call.fly()
    
parr= Parrot()
Pengu= Penguin()
Called(parr)
Called(Pengu)



#mulevel inheritance
class A:
    a= "thi is a Class"
class B(A):
    b= "this is b class"

class C(B):
    c= "this is c Class"

b_instance= B()
print(b_instance.a)

class D(C):
    d= "this is d Class"

class E(D):
    pass

obj = E()

# print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)


# multiple inheritance

class A:
    def __init__(self) -> None:
        pass

    def a(self):
        print("this is Class A with multiple inheritance")

class B:
    def __init__(self) -> None:
        pass

    def b(self):
        print("this is class b with multiple inheritance")


class C(A,B):
    def __init__(self) -> None:
        super().__init__()


instance_of_class_c= C()
instance_of_class_c.a()
instance_of_class_c.b()