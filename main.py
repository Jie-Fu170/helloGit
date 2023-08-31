def quicksort(arr):
   if len(arr) <= 1:
       return arr
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x < pivot]
   middle = [x for x in arr if x == pivot]
   right = [x for x in arr if x > pivot]
   return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
print("hello")
#堆排序
def heapify(arr, n, i):
   largest = i
   left = 2 * i + 1
   right = 2 * i + 2

   if left < n and arr[left] > arr[largest]:
       largest = left

   if right < n and arr[right] > arr[largest]:
       largest = right

   if largest != i:
       arr[i], arr[largest] = arr[largest], arr[i]
       heapify(arr, n, largest)

def heap_sort(arr):
   n = len(arr)

   # 构建大顶堆
   for i in range(n // 2 - 1, -1, -1):
       heapify(arr, n, i)

   # 逐个提取元素
   for i in range(n - 1, 0, -1):
       arr[i], arr[0] = arr[0], arr[i]
       heapify(arr, i, 0)

   return arr

print(heap_sort([12, 11, 13, 5, 6, 7]))