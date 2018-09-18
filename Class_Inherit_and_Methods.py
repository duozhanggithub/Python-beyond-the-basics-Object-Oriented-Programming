#class inherit

class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print ('%s is eating %s.' %(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s.' %(self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print('%s shred the string!' %(self.name))

dog = Dog('Rover')
cat = Cat('fluffy')

dog.fetch('paper')
cat.swatstring()
dog.eat('dog food')
cat.eat('cat food')
dog.swatstring()

#multiple inherit

class A(object):
    def dothis(self):
        print ('do this in A')

class B(A):
    pass

class C(A):
    def dothis(self):
        print('do this in C')

class D(B,C):
    pass

d_instance = D()
d_instance.dothis()

print(D.mro())

#instance method, class method and static method, notice the decorators

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    def __set__(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    @classmethod
    def get_count(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('aa')

for obj in (a,b,c):
    print('val of obj: %s' % (obj.get_val()))
    print('count: %s' % (obj.get_count()))
