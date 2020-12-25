from SingletonMath import MathClass

class Math(MathClass):
    def sqrt(self,x):
        if (x == 0 and x == 1):
            return x
        
        i = 1
        result = 1
        while(result <= x):
            i+=1
            result = i*i

        return (float(i-1))
    
    

    '''
    设置一个精准度1/3
    接着使用传入进来的值，弄成x^1/3次方，最后使用round函数，将舍入到1位精度的值，得到最后开三次方结果。
    其他解法如下:
    1.最小二乘法 梯度
    2.牛顿不动点迭代法
    
    '''
    def cubic(self,x):
        return round(x**(1/3),1) #

if __name__ == "__main__":
    x = input() #默认类型为str,需要转换类型
    x = int(x)
    mathRest = Math()
    
    print(Math.sqrt(mathRest,x))
    print(Math.cubic(mathRest,x))