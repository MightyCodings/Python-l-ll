for n in range (1,501):
    s=0
    for i in range(1,n):
        t=n
        while n>0:
            r=n%10
            s=s*10+r
            n=int(n/10)
        if s==t:
            print(s)    
