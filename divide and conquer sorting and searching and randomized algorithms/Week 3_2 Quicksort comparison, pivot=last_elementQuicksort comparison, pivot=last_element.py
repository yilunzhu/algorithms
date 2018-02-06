def quicksort(A, i, j, calculator):
    if i>=j:
        return calculator
    else:
        q, calculator=partition(A, i, j, calculator)
        calculator=quicksort(A, i, q-1, calculator)
        calculator=quicksort(A, q+1, j, calculator)
        return calculator

def partition(A, left, right, calculator):
    pivot=A[right]
    i=left
    for j in range(left, right):
        calculator+=1
        if A[j] <= pivot:
            A[i],A[j]=A[j],A[i]
            i+=1
        else:
            continue
    A[right], A[i] = A[i], A[right]
    return i, calculator

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