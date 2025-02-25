n=int(input("enter anu"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if s==1:
    print("prime")  
else:    
    print("not prime")
    

