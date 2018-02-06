heap_size = 0

def MaxHeapify (A, i):
    global l
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest)

def BuildHeap(A):
    global heap_size
    heap_size = len(A)
    for i in range(len(A)//2-1, -1, -1):
        MaxHeapify(A, i)

def HeapSort(A):
    global heap_size
    BuildHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        MaxHeapify(A, 0)

if __name__=="__main__":
    Array = [18, 37, 46, 24, 5, 98, 77, 1, 14, 57]
    BuildHeap(Array)
    print(Array)
    HeapSort(Array)
    print(Array)