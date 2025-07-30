c1 = float(input("enter the speed (km/h) of the 1st cyclist"))
c2 = float(input("enter the speed (km/h) of the 2nd cyclist"))
c3 = float(input("enter the speed (km/h) of the 3rd cyclist"))

avg_speed = (c1 + c2 + c3) / 3

print("average speed",avg_speed,"km/h")
if c1 < avg_speed:
    print("speed of cyclist 1 is slower than average with the differance of:",avg_speed - c1 )


if c2 < avg_speed:
    print("speed of cyclist 2 is slower than average with the differance of:",avg_speed - c2 )

if c3 < avg_speed:
    print("speed of cyclist 3 is slower than average with the differance of:",avg_speed - c3 )