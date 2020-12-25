from abc import ABC,ABCMeta,abstractmethod  
class Math:
    @abstractmethod
    def sqrtnewton(self,n,l):
        pass    

if __name__ == "__main__":
    n = 327
    l = 0.00001 #精准度
    res = RelalizeInterface.sqrtnewton(n,l)
    print(res)