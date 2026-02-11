a=int(input("enter first number"))
b=int(input("enter second number"))
caal=int(input(""""operation you want
    1:addition
    2:subtraction
    3:multiplicaton
    4:division"""))
match caal:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("invaild")
