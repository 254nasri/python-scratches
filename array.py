print("\n\nwelcome to my array\n")
x=0
no=int(input("no of cars: "))
print(no)
cars_array=[]
while no!=x:
    name=input("car: ")
    cars_array.append(name)
    x=x+1
def mycars():
    cars = len(cars_array)
    print("\nThe array contains: {} cars".format(cars))
    cars = cars + 1
    y = 1
    print("\ncars in the array:\n")
    while cars != y:
        print("{}.{}".format(y, cars_array[y - 1]))
        y = y + 1
mycars()
print("\nOperations on array:\n")
print("1.delete item\n2.add item\n3.reverse list\n4.insert item at specified position\n5.clear array")
choice=int(input("option: "))
a=1
while a==1:
    if choice==1:
        posn=int(input("\nEnter position of car to delete: "))
        posn=posn-1
        cars_array.pop(posn)
        print("updated array:")
        mycars()
        break
    elif choice==2:
        type=input("Name of car to add: ")
        cars_array.append(type)
        print("updated array:")
        mycars()
        break
    elif choice==3:
        cars_array.reverse()
        mycars()
        break
    elif choice==4:
        posn=int(input("current position: "))
        print()
        posn=posn-1
        car=cars_array[posn]
        move=int(input("preferred position: "))
        print()
        cars_array.insert(move,car)
        mycars()
    elif choice==5:
        cars_array.clear()
        print("items in the array cleared successfully")
        break

    else:
        print("invalid command!!!!")
        break
