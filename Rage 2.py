for n in range (1,10000):
    sum=0
    for i in range(1,10000):
     t=n
    while n>0:
        r=n%10
        sum=sum+(r*r*r*r)
        n=int (n/10)
    if sum==t:
     print(t)