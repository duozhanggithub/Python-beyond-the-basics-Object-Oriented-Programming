#override/overload: child's own version of a method
#extend: do work in addition to taht in parent's method
#provide: implement method that parent class requires

import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self,value):
        self.val = 0
    def set_val(self, value):
        self.val = value
    def get_val(self):
        return self.val
    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):

    #specializing
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
            super(GetSetInt, self).set_val(value)
    def showdoc(self):
        print('GetSetInt object ({0}), only accepts '
              'integer values'.format(id(self)))

#polymorphic
class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print('GetSetList object len{0}, stores '
              'history of values set'.format(len(self.vallist)))

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()