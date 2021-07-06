print("*****************************")
print("******my calculator**********")
print("*****************************")
print()
a=int(input("1st integer: "))
while 1:
    b=input("operator: ")
    c=int(input("2nd integer: "))
    if b=="*":
        d=a*c
        print("\nAns= ",d)
        print()
        a=d
    elif b=="+":
        d=a+c
        print("\nAns= ",d)
        print()
        a=d
    elif b=="-":
        d=a-c
        print("\nAns= ",d)
        print()
        a=d
    elif b=="/":
        d=a/c
        print("\n Ans= ",d)
        print()
        a=d
    else:
        print("wrong operator")
        break
