def diff(n, mid) : 
    if (n > (mid * mid * mid)) : 
        return (n - (mid * mid * mid)) 
    else : 
        return ((mid * mid * mid) - n) 
          
# Returns cube root of a no n 
def cubicRoot(n) : 
      
    # Set start and end for binary  
    # search 
    start = 0
    end = n 
      
    # Set precision 
    e = 0.0000001
    while (True) : 
          
        mid = (start + end) / 2
        error = diff(n, mid) 
  
        # If error is less than e  
        # then mid is our answer 
        # so return mid 
        if (error <= e) : 
            return mid 
              
        # If mid*mid*mid is greater 
        # than n set end = mid 
        if ((mid * mid * mid) > n) : 
            end = mid 
              
        # If mid*mid*mid is less  
        # than n set start = mid 
        else : 
            start = mid


    # def binarySerarchCubicNumber(n):

    #     low = 0
    #     high = n
        
    #     ## 设置数值精度
    #     e = 0.0000001

    #     while(low < high):
    #         mid = (low+high) / 2
    #         error = diff(n,mid)

    #         '''
    #         如果error是小于e的话，那mid就是开完立方后的数字
    #         '''
    #         if(error <= e):
    #             return mid
            
    #         '''
    #         如果mid^3是比较大的，则n就需要设置为low = mid
    #         '''

    #         if((mid*mid*mid) > n):
    #             high = mid
    #         else:
    #             low = mid

n = 216
print("Cubic root of", n, "is",  
      round(cubicRoot(n),1))