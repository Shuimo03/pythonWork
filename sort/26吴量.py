'''
排序算法中有一个稳定性，稳定性是指能保证排序前2个相等的数其在序列的前后位置顺序和排序后它们两个的前后位置顺序相同。
在简单形式化一下，如果Ai = Aj，Ai原来在位置前，排序后Ai还是要在Aj位置前。
稳定性算法如下:
1. 冒泡排序
2. 插入排序
3. 基数排序

不稳定排序算法：
1. 选择排序
2. 快速排序
3. 希尔排序
4. 堆排序
'''

import sys
import timeit

'''
 冒泡排序是一种简单排序算法，它重复的遍历待排序的数列，一次比较两个元素，
 按照一定规则进行比较然后交换元素，等全部排序完之后，算法结束，冒泡排序对n
 个元素想要O(N^2)比较次数，并且可以原地排序。
'''

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

'''
插入排序的工作原理是通过构建有序序列，对于未排序数据，在已经排好序的序列中，从后
前扫描，找到相应位置并插入，插入排序需要额外的O(1)空间，因而在从后向前扫描过程中，
需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
插入排序的时间复杂度是O(N^2)
'''

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

'''
基数排序是一种非比较型整数排序算法，其原理是将整数按位切割成不同的数字，
然后按每个位数分别比较，基数排序不限于整数范围，同时也支持字符串和特定格式
的浮点数。

时间复杂度O(kN)
空间复杂度O(k+N)
'''

def countingSort(arr,exp1):
    n = len(arr)

    output = [0]*(n)
    count  = [0]*(10)

    for i in range(0,n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr,exp)
        exp *= 10


'''
选择排序的工作原理如下，首先在未排序序列中找到最小或最大元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最大或最小元素，然后放在已排序序列的末尾，以此类推，
知道所有元素排序完成。
时间复杂度O(N^2)
空间复杂度O(N)
'''

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]


'''
快速排序使用分治法策略，将一个数组或者序列分为较小和较大的两个子序列，然后递归的排序两个子序列
步骤为：

1. 挑选基准值：从数列中挑出一个元素，称为“基准”（pivot），
2. 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成，
3 .递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。

时间复杂度O(nlogn)
'''

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] < pivot:

            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

'''
希尔排序（Shellsort），也称递减增量排序算法，是插入排序的一种更高效的改进版本。
希尔排序是非稳定排序算法, 时间复杂度O(N),空间复杂度O(N)
'''

def shellSort(arr):

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap,n):
           
           temp = arr[i]
           
           j = i
        while j >= gap and arr[j-gap] > temp:
            arr[j] = arr[j-gap]
            j -= gap

            arr[j] = tmep
        
        gap //= 2


'''
堆排序（英语：Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆的性质：
即子节点的键值或索引总是小于（或者大于）它的父节点。
时间复杂度O(nlogn)
'''

def heapify(arr,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        heapify(arr,n,largest)

def heapSort(arr):

    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


'''
Merge sort 是创建归并操作上的有效排序，时间复杂度在0(nlogn)，空间复杂度在O(n)
'''

def mergeSort(arr):
    if len(arr) > 1:
        
        #在数组中查找中间值
        mid = len(arr) // 2

        #分割数据元素
        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len (L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i  < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


if __name__ == "__main__":
    #arr = [64, 34, 25, 12, 22, 11, 90]
    arrElements = input()
    arr = [int(n) for n in arrElements.split()]
    print("未排序数组:",arr)

    print("-----------------------")

    Start = timeit.default_timer()
    bubbleSort(arr)
    Stop = timeit.default_timer()
    print("BubbleSort:",arr)
    print("运算时间:",Stop-Start)

    print("-----------------------")

    insertStart = timeit.default_timer()
    insertionSort(arr)
    insertStop = timeit.default_timer()
    print("insertionSort:",arr)
    print("运算时间:",insertStop-insertStart)
    
    print("-----------------------")

    radStart = timeit.default_timer()
    radixSort(arr)
    radStop = timeit.default_timer()
    print("radixSort:",arr)
    print("运算时间:",radStop-radStart)

    print("-----------------------")
    selectStart = timeit.default_timer()
    selectionSort(arr)
    selectStop  = timeit.default_timer()
    print("selectionSort",arr)
    print("运算时间:",selectStop-selectStart)
    
    print("-----------------------")

    quickStart = timeit.default_timer()
    n = len(arr)
    quickSort(arr,0,n-1)
    quickStop = timeit.default_timer()
    print("quickSort:",arr)
    print("运算时间:",quickStop-quickStart)


    print("-----------------------")
    shellStart = timeit.default_timer()
    shellSort(arr)
    shellStop = timeit.default_timer()
    print("shellSort:",arr)
    print("运行时间:",shellStop-shellStart)
    
    print("-----------------------")
    heapStart = timeit.default_timer()
    heapSort(arr)
    heapStop  = timeit.default_timer()
    print("heapSort",arr)
    print("运行时间:",heapStop-heapStart)
    
    
    print("-----------------------") 
    mergeStart = timeit.default_timer()
    mergeSort(arr)
    mergeStop = timeit.default_timer()
    print("mergeSort:",arr)
    print("运行时间:",mergeStop-mergeStart)
    print("-----------------------")