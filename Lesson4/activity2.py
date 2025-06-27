amount = int(input("what is the amount: "))


note_100 = amount // 100
amount = amount % 100

note_50 = amount // 50
amount = amount % 50

note_10 = amount // 10 

print(note_100)
print(note_50)
print(note_10)