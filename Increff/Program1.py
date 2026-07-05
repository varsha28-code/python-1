s="CAT"
n=3
a=[1,4,7]
def solve(s,n,a):
    count=0
    digit_set=set(a)
    for ch in s:
        asc_s=str(ord(ch))
        for dig in asc_s:
            if int(dig) in digit_set:
                count+=1
                break
    print(count)
solve(s,n,a)
