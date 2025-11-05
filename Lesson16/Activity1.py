def factorial(x):
    '''this is a recursive function to find the factorial of a integer'''

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("the factoorial of0:",factorial(0))
print("the factoorial of07:",factorial(7))
print("the factoorial of14:",factorial(14))
print("the factoorial of21:",factorial(21))
print("the factoorial of28:",factorial(28))


