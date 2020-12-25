#递归 Fibonacci number
def fib(n):
    if n <= 0:
        print("输入错误")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(13))