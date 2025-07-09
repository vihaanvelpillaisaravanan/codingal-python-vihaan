a = 10
b = 12
c = 10

if a and b and c:
    print("all the number have the boolean true")
else:
    print("at least one number has the boolean false")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("at least one number is greater than zero")
else:
    print("no numbers are greater than zero")


if b > 0 or c == 0:
    print("at least one number is greater than or equal to 0")
else:
    print("no numbers are greater than or equal to 0")
