medical_cause = input("enter medical cause['y'] for yes and ['n']for no: ")

if medical_cause.lower() == "y":
    print("you are allowed!")
else:
    atendence = int(input("enter your attendence: "))
    if atendence > 75:
        print("you are allowed")

    else:
        print("you are not allowed!")