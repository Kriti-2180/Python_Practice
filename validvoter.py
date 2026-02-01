name=input("enter your name : ")
age=int(input("enter your age : "))
if age > 18:
    print(f"hello {name} you are a valid voter")
else:
    print(f"hello {name} you are not a valid voter but you can vote after {18-age} years")