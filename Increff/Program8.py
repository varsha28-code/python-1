def min_1(n):
    n=abs(n)
    if n==0:
        return 0
    def helper(x):
        if x==0:
            return 0
        s=str(x)
        k=len(s)
        R=int('1'*k)
        if R==x:
            return k 
        if R>x:
            k-=1
            R=int('1'*k)
        m=x//R
        rem1=x-m*R 
        rem2=(m+1)*R-x
        first_try=m*k+helper(rem1)
        if rem2<x:
            sec_try=(m+1)*k+helper(rem2)
            return min(first_try,sec_try)
        else:
            return first_try
    return helper(n)
print(min_1(32))
