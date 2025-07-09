weight = float(input("enter your weight in kgs: "))
height = float(input("enter your height in M: "))

BMI = weight / (height ** 2)
print(BMI)

if BMI < 18.5:
    print("you are under weight")
elif BMI >= 18.5 and  BMI <= 24.9:
    print("you are healthy")
else:
    print("you are over weight")
