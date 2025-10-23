def add(P,Q):
    return P + Q
def sub(P,Q):
    return P - Q
def mul(P,Q):
    return P * Q
def div(P,Q):
    return P/Q
print("please enter your choice of operation")
print("A, add")
print("S, subtract")
print("M, multiply")
print("D, divide")

choice = input("choose your operation,(A/S/M/D): ")

num1 = print("please enter your first number: ")
num2 = print("please enter your secong number: ")

if choice == 'A':
    print(num1, "+", num2,"=",add(num1,num2))
elif choice == 'S':
    print(sub(num1,num2))
elif choice == 'M':
    print(mul(num1,num2))
elif choice == 'D':
    print(div(num1,num2))
else:
    print("invalid input")

