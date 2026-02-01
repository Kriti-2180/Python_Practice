n=int(input("enter no: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("no. is prime no.")
else:
    print("no. is not prime no.")