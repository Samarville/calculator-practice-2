def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("selection operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

choice=input("Enter  choice 1/2/3/4:")
num1=float(input("Enter first desired number:"))
num2=float(input("Enter desired second number:"))

if choice=='1':
    print(num1,"+", num2, "=", add(num1,num2))
elif choice=='2':
    print(num1,"-",num2, "=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*", num2,"=", multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",division(num1,num2))
else:
        print("the number invalid")

