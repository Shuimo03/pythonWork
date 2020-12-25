from abc import ABCMeta,abstractclassmethod

class MathClass(metaclass=ABCMeta):    
    @abstractclassmethod
    def sqrt(self,x):pass
    @abstractclassmethod
    def cubic(self,n):pass
