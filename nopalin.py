n=int(input("enter no: "))
rev=0
copyn=n
while n > 0:
    rev=rev*10+n%10
    n=n//10
if copyn==rev:
    print("Palindrome no.")
else:
    print("Not a palindrome no.")    