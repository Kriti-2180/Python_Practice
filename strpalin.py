a=input("enter string : ")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
if b==a:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome")