num = int(input("enterr the number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    factor = 2

    while factor < num:


        if num % factor == 0:
            is_prime = False
            break
        factor += 1
if is_prime:
    print(num,"is  prime")
else:
    print(num,"is not prime")