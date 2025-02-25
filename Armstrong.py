n=int(input("Enter any Number:\n\a"))
sum=0
t=n
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=int(n/10)
if sum==t:
    print("Number is Armstrong\n\a")
else:
    print("Number is not Armstrong\n\a")    
   
    