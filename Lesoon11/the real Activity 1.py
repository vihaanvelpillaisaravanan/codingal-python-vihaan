nth = int(input("enter this nth number: "))

i = 1
sum = 0

while i <= nth:
    print(i)
    sum = sum + i
    i = i + 1


print(f"sum of the{nth} natural numbers is: {sum}")