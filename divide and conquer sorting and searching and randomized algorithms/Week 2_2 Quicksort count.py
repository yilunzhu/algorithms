def quicksort(A, i, j):
    if j-i<=1:
        return
    else:
        q=partition(A, i, j)
        quicksort(A, i, q)
        quicksort(A, q+1, j)

def partition(A, left, right):
    pivot=A[left]
    i=left+1
    for j in range(left+1, right+1):
        if A[j] < pivot:
            A[i],A[j]=A[j],A[i]
            i+=1
        else:
            continue
    A[left],A[i-1]=A[i-1],A[left]
    return i-1

file=open('QuickSort.txt')
words=file.readlines()
numbers=[]
for num in words:
    n=num.rstrip('\n')
    numbers.append(int(n))
quicksort(numbers,0, len(numbers)-1)
print(numbers)
#testcode_1
#A=[3,5,8,4,2,1]
#quicksort(A,0,6)