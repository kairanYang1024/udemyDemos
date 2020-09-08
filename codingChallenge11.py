# Still having issues with updating the dictionary

pricelist = {}  # empty dict

termination = "c"  # continue
while termination != "e" :   # exit
    product_name = input("Please enter the product name on the shelf \n")
    product_price = int(input("Please enter the product price of " +
                              product_name + "\n"))
    pricelist[product_name] = product_price # assign the pair to dictionary
    termination = input("End? (press e or not)\n")
print("The price list after discount is: ")

pricelist_disc = list(map(lambda price : price - 10 * (price / 100),
                          pricelist.values()))
print(list(pricelist_disc))
