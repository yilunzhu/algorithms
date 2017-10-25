#Assignment_1, Karatsuba Mutiplication
'''def karatsuba_mutiplication(x,y):
    length=max(len(str(x)),len(str(y)))
    if len(str(x))==1 or len(str(y))==1:
        return x*y
    else:
        num_split=length//2
        a=int(x)//10**num_split
        b=int(x)%10**num_split
        c=int(y)//10**num_split
        d=int(y)%10**num_split
        ac=karatsuba_mutiplication(a,c)
        bd=karatsuba_mutiplication(b,d)
        ad_plus_bc=karatsuba_mutiplication(a+b,c+d)-ac-bd
        product=ac*(10**(2*num_split))+ad_plus_bc*(10**num_split)+bd
        return product

m=input("The first number is:\n")
#3141592653589793238462643383279502884197169399375105820974944592
n=input("The second number is:\n")
#2718281828459045235360287471352662497757247093699959574966967627
result=karatsuba_mutiplication(m,n)
print(result)'''


#Assignment 2, Count and Split
'''def Count_and_inversions(array,n):
    if n==1:
        return 0
    else:
        split=int(n/2)
        leftarray=array[:split]
        rightarray=array[split:]
        new_array=[]

        #Count_and_inversions(leftarray,n/2)
        #Count_and_inversions(rightarray,n/2)

        i=0
        j=0
        count=0
        for k in range(n):
            if leftarray[i]<=rightarray[j]:
                new_array[k]=leftarray[i]
                i+=1
                count+=1
            else:
                new_array[k]=rightarray[j]
                j+=1
                count+=1
    return count'''
#test code 1
'''file=open('IntegerArray.txt')
b=file.readlines()
length=len(b)
c=[]
for i in range(length):
    c.append(int(b[i]))'''
#test code 2
'''ls=[1, 4, 2, 8, 5, 7]'''


#Quicksort count
'''def quicksort(A, i, j):
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
#quicksort(A,0,6)'''

#Assignment_3.1_Quicksort comparison
'''def quicksort(A, i, j, calculator):
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
print(count)'''

#Assignment_3.2_Quicksort comparison, pivot=last_element
'''def quicksort(A, i, j, calculator):
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
print(a)'''

#Assignment_3.2_Quicksort comparison, pivot=median
''''# import math

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
print(a)'''

#Assignment_4, Karger min cut
import random, copy
data = open("kargerMinCut.txt","r")
G = {}
for line in data:
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0]

def operation(n):
    i = 0
    count = 10000
    while i < n:
        data = copy.deepcopy(G)
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count

if __name__=="__main__":
    print(operation(100))




