import sys

#list of exempted element: book, foods, medical products
exemptedList = ["book", "chocolate", "headache pills"]


def appliedTaxesPrice(rawPrice, quantity, isExempted, isImported):
    """
   Compute taxes on good prices: imported goods + 5%; not exempted food 10%

   :param str rawPrice: not taxed priced in string
   :param str quantity: number of items in stirng
   :param Bool isExempted: True if good is in the list exmptedList
   :param Bool isImported: True if good is imported
   :return: applied taxes price
   """

    appliedTaxesPrice = float(rawPrice)
    
    #import duty
    if isImported:
        appliedTaxesPrice += roundingRulePrice(0.05*float(rawPrice))

    #basic sales tax
    if not(isExempted):
        appliedTaxesPrice += roundingRulePrice(0.1*float(rawPrice))


        
    
    return float(quantity)*appliedTaxesPrice
    
def roundingRulePrice(appliedTaxesPrice):
    """
   a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax

   :param float appliedTaxesPrice: not rounded applied taxes price
   """
    return round(appliedTaxesPrice / 0.05) * 0.05

for filename in sys.argv[1:]:
    print("OUTPUT " + filename)
    # read input from files
    f = open(filename ,"r+")
    lines = f.readlines()

    totalTaxedPrice = 0
    totalRawPrice = 0

    for line in lines:
        splitAt = line.split(" at ")
        splitSpace = splitAt[0].split(" ", 1)

        quantity = splitSpace[0]
        good = splitSpace[1]

        rawPrice = splitAt[1]

        # check if good is imported
        isImported = "imported" in good

        # check if good is book, foods, medical products
        isExempted = False
        for exemptedGood in exemptedList:

            if exemptedGood in good:
                isExempted = True
                break
        
        price = appliedTaxesPrice(rawPrice, quantity, isExempted, isImported)

        print(splitAt[0] + " " + "{:.2f}".format((round(price, 2))))
        totalTaxedPrice += float(price)
        totalRawPrice += float(quantity)*float(rawPrice)

    # computed sales taxes
    totalSalesTaxes = totalTaxedPrice - totalRawPrice
    
    print("Sales Taxes: " + "{:.2f}".format(round(totalSalesTaxes, 2)))
    print("Total: " + "{:.2f}".format(round(totalRawPrice + totalSalesTaxes, 2)) + "\n")

    f.close()