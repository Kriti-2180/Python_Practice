n=int(input("enter no: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("no. is perfect")
else:
    print("no. is not perfect")