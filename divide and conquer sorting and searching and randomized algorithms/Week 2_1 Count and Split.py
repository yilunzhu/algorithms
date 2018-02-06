def Count_and_inversions(array,n):
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
    return count

#test code 1
'''file=open('IntegerArray.txt')
b=file.readlines()
length=len(b)
c=[]
for i in range(length):
    c.append(int(b[i]))'''
#test code 2
#ls=[1, 4, 2, 8, 5, 7]