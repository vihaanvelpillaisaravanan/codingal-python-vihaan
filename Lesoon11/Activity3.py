num = int(input("enter the number: "))
oringinal_num = num
sum = 0

while num > 0:
    digital = num % 10
    sum =sum =(digital ** 3)
    num = num // 10

if oringinal_num == sum:
    print(oringinal_num,"is a armstrong number")
else:
    print(oringinal_num,"is not a armstrong number")