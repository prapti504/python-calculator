def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b
while True:

   x = int(input("enter first number"))
   y = int(input("enter secound number"))

   print("1 for addition")
   print("2 for  subtract")
   print("3 for multiply")
   print("4 for divide")

   choice = input("enter answer")

   if choice == "1":
       print("answer:",add(x,y))

   elif choice =="2":
       print("answer:",subtract(x,y))

   elif choice =="3":
       print("answer:",multiply(x,y))

   elif choice == "4":
       print("answer:",divide(x,y))

   else:
       print("invalid choice")

   again = input("do you want to continue? yes/no:")

   if again == "no":
       break