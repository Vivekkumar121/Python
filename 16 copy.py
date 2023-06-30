a = int(input("ENter number a"))
b = int(input("Enter number b"))
x = int(input("Enter your choice "))
match x :
    case 1 :  print(a + b)
    case 2 : print(a - b)
    case 3 : print(a * b)
    case 4 : print(a / b)
    case _ : "this is default number"