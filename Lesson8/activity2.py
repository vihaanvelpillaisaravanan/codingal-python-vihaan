numerator = int(input("enter the numerator: "))
denominator = int(input("enter the denominator: "))

if numerator % denominator == 0:
    print(f"{numerator}is divisable by the {denominator}")
else:
    print(f"\{numerator} is not divisable by the {denominator}")