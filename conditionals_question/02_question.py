age =  int(input("please enter your age:"))
day = (input("please enter day :"))

price = 0
discount = 0
if (age>18):
    price = 12
    if (day == "wednesday"):
        discount = 2
        print(f"price is {price} - {discount}(discount) = {price - discount}")
    else:
        print(f"price is {price} - {discount}(discount) = {price - discount}")
else:
    price = 8
    if (day == "wednesday"):
        discount = 2
        print(f"price is {price} - {discount}(discount) = {price - discount}")
    else:
        print(f"price is {price} - {discount}(discount) = {price - discount}")