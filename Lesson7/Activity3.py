mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

total = mark1 + mark2 + mark3 + mark4 + mark5
avg = total / 5

if avg >= 91 and avg <= 100:
    print("A1")
elif avg >= 81 and avg < 91:
    print("A2")
elif avg >= 71 and avg < 81:
    print("B1")
elif avg >= 61 and avg < 71:
    print("B2")
elif avg >= 51 and avg < 61:
    print("C1")
elif avg >= 41 and avg < 51:
    print("C2")
elif avg >= 31 and avg < 41:
    print("D1")
elif avg >= 21 and avg < 31:
    print("D2")
elif avg >= 11 and avg < 21:
    print("E1")
elif avg >= 1 and avg < 11:
    print("E2")
else:
    print("Error 404")