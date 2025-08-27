text = input("ENter the text")
char = input("enter the character: ")

count = 0

for x in text:
    if x.lower() == char.lower():
        count += 1

print(char,"appears",count,"times")