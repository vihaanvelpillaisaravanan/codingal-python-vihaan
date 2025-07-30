a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print(f"a = {a}, b = {b}, c = {c}")

a, b, c = c, a, b

print("\nAfter circular swapping (a → b, b → c, c → a):")
print(f"a = {a}, b = {b}, c = {c}")