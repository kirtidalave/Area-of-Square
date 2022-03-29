def area_rect(x,y):
    return x*y

def perimeter_rect(x,y):
    return 2*(x+y)

def area_square(x):
    return x*x


if __name__=="__main__":

    n1 = int(input(" number 1: "))
    n2 = int(input("number 2: "))
    print("1. Area of Rectangle :")
    print("2. Perimeter of Rectangle:")
    print("3. Area of Square :")
    ch=int(input("enter your choice"))
    if ch==1:
        print(area_rect(n1,n2))
    elif ch==2:
        print(perimeter_rect(n1,n2))
    elif ch==3:
        print(area_square(n1))
    else:
        print("Invalid choice")
