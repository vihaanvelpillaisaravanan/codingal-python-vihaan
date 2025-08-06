string = input("enter the string: ")


print ("directly finding reversed string: ",string[::-1])

print("\n------------------------\n")


reversed_string = ""
for letter in string:
    print(letter)
    reversed_string = letter + reversed_string
    print(reversed_string)

print("reversed string using for loop: ",reversed_string)