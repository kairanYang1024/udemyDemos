def getPrices(priceTags, key):
    return priceTags.get(key)

pricelist = {"Banana": 20, "Flower Pot":55, "KFC":102, "Nintendo Switch":10000, "Sprite":70}
print("Welcome to the store")
product = ""
while product.lower() != "end":
    print("We have those products on sale: ",  list(pricelist.keys()))
    product = input("Enter which one you want to buy: ")
    if product in pricelist:
        print("The price of ", product, " is ", getPrices(pricelist, product))
    elif product.lower() == "end":
        print("Thank you for coming!")
        break
    else:
        print("Sorry, the product ", product, " you entered is not in the list")
