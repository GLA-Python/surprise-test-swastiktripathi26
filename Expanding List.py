def expanding(a):
    c=len(a)
    lst=[]
    for i in range(c-1):
        d=a[i]-a[i+1]
        lst.append(abs(d))
    m=0
    for i in range(len(lst)-1):
        if lst[i+1]>lst[i]:
            m+=1
    if m==len(lst)-1:
        return True
    else:
        return False
a=eval(input())
out=expanding(a)
print(out)