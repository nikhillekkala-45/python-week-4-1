a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
print("maximum number is")
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
print("minimum number is")
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)
