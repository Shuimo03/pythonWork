'''
第一种方式是使用切片
'''

def reverse(List):
    return List[::-1]


'''
第二种方式使用双指针方式，分别设置两个指针，指向列表头和列表尾，
交换两个指针对应的元素，并且更新指针位置，直到两个指针相遇，表示
遍历结束，时间复杂度O(N)
'''

def doublePoint(List):
    l = 0
    r = len(List)-1

    while l < r:
        List[l],List[r] = List[r],List[l]
        l+=1
        r-=1
    return List    

# 第三种
def reverseString(List):
    for i in range(len(List)//2):
            List[i],List[-i-1]=List[-i-1],List[i]
    return List
    

#递归写法
def reverseStr(List):
    if len(List) <=1:
        return List
    else:
        return reverseStr(List[1:])+[List[0]]



if __name__ == "__main__":
    num = input()
    arr =  [str(n) for n in num.split()]
    strarr = [str(n) for n in num.split()]
    print(reverseStr(arr))
    print(doublePoint(arr))
    print(reverse(strarr))
    print(reverseStr(strarr))
