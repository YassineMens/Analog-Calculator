print("Select operation.")
print("1.+")
print("2.-")
print("3.X")
print("4.:")


choice = input("Enter choice(1/2/3/4): ")
if choice == "1":
    x = input("enter first number >> ")
    y = input("enter first number >> ")
    xy = int(x) + int(y)
    print(xy)

if choice == "2":
    x = input("enter first number >> ")
    y = input("enter first number >> ")
    xy = int(x) - int(y)
    print(xy)
if choice == "3":
    x = input("enter first number >> ")
    y = input("enter first number >> ")
    xy = int(x) * int(y)
    print(xy)
if choice == "4":
    x = input("enter first number >> ")
    y = input("enter first number >> ")
    xy = int(x) / int(y)
    print(xy)