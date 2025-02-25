n=int(input("Enter any Number:"))
sum=0
t=n
while n>0:
    r=n%10
    sum=sum*10+r
    n=int(n/10)
if sum==t:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")    
   
    