# def sqrtNewton(n,l):
    
    # x = n
    # count = 0

    # while (1):
    #     count+=1
    #     root = 0.5 * (x+(n/x))
    #     if(abs(root-x) < l):
    #         break
        
    #     x = root

    # return root
# if __name__ == "__main__" :  
  
#     n = 327
#     l = 0.00001 #精准度
  
#     print(sqrtNewton(n, l)) 

from NewtonABC import Math
class test(Math):
   def sqrtnewton(self,n,l):
    x = n
    count = 0

    while (1):
        count+=1
        root = 0.5 * (x+(n/x))
        if(abs(root-x) < l):
            break
        
        x = root

    return root

if __name__ == "__main__":
    n = 327
    l = 0.00001 #精准度
    print(test.sqrtNewton(n, l)) 