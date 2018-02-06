def quicksort(A, i, j, calculator):
    if i>=j:
        return calculator
    else:
        q, calculator=partition(A, i, j, calculator)
        calculator=quicksort(A, i, q-1, calculator)
        calculator=quicksort(A, q+1, j, calculator)
        return calculator

def partition(A, left, right, calculator):
    pivot=A[left]
    i=left+1
    for j in range(left+1, right+1):
        calculator+=1
        if A[j] < pivot:
            A[i],A[j]=A[j],A[i]
            i+=1
        else:
            continue
    A[left],A[i-1]=A[i-1],A[left]
    return i-1, calculator

file=open('QuickSort.txt')
words=file.readlines()
numbers=[]
for num in words:
    n=num.rstrip('\n')
    numbers.append(int(n))
count=quicksort(numbers,0, len(numbers)-1, 0)
#a=[8,1,3,5,2,4,7,10,6,9]
print(numbers)
print(count)