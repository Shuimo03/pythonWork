# import timeit

# bubble_start = timeit.default_timer()

# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]

# bubble_stop = timeit.default_number()

# print(bubble_stop-bubble_start)

import timeit

def bubbleSort(arr):
    start = timeit.default_timer()
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    stop = timeit.default_timer()
    print('Time: ', stop - start) 


arr = [6,5,3,2,1]

bubbleSort(arr)