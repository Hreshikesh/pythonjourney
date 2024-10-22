#sum of digits
sum=0
n=int(input("Enter the number"))
while(n!=0):
    r=n%10
    sum+=r
    n=n//10
    print(n)
print(f"Sum ={sum}")