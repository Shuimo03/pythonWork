from abc import ABCMeta, abstractclassmethod

#定义数学接口
class mathInterFace(metaclass=ABCMeta):
     @abstractclassmethod
     def sqrt(self,x):pass
     @abstractclassmethod
     def cubic(self,x):pass

#实现接口
class mathTest(mathInterFace):
    def sqrt(self,x):
        return x
    
    def cubic(self,a,n=3):


if __name__ == "__main__":
    Math = mathTest()
    print(mathTest.cubic(Math,8))
