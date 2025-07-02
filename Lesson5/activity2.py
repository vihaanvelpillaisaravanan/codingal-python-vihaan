actual_price = float(input("what is the actual price of the product: "))
sale_price = float(input("what is the sale of the product"))

if sale_price > actual_price:
    print("profit",sale_price-actual_price)

else:
    print("no proft!!")



