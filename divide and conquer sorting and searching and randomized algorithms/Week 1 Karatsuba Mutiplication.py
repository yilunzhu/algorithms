def karatsuba_mutiplication(x,y):
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
print(result)