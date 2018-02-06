# import math

def quicksort(A, i, j, calculator):
    if i>=j:
        return calculator
    else:
        calculator+=1
        q, calculator=partition(A, i, j, calculator)
        calculator=quicksort(A, i, q-1, calculator)
        calculator=quicksort(A, q+1, j, calculator)
        return calculator

def is_median(A, left, right):
    median = left + math.floor((right - left) / 2)
    if ((A[median] < A[right] and A[right] < A[left]) or (A[left] < A[right] and A[right] < A[median])):
        return right
    elif ((A[right] < A[left] and A[left] < A[median]) or (A[median] < A[left] and A[left] < A[right])):
        return left
    else:
        return median

def partition(A, left, right, calculator):
    pivot=A[is_median(A, left, right)]
    i=left
    for j in range(left, right+1):
        calculator+=1
        if A[j] <= pivot:
            A[i],A[j]=A[j],A[i]
            i+=1
        else:
            continue
    A[left], A[i-1] = A[i-1], A[left]
    return i-1, calculator

file=open('QuickSort.txt')
words=file.readlines()
numbers=[]
for num in words:
    n=num.rstrip('\n')
    numbers.append(int(n))
count=quicksort(numbers, 0, len(numbers)-1, 0)
print(numbers)
print(count)
a=[3,6,4,1,5,2]
quicksort(a, 0, 5, 0)
print(a)