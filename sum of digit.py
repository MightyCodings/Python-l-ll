n=int(input("Enter any Number:"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=int(n/10)
print(s)    