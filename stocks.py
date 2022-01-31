#CS175L-01
#Ez Racancoj
#stocks

commissionRate = float(input('what aws the commission rate '))
#.03
numShares = float(input('how many shares did you purchasee '))
#2000
purchasePrice = float(input('What was the cost of each of the shares '))
#40
sellingPrice = float(input('How much did you sell them at '))
#42.75
amountPaidForStock = numShares * purchasePrice

purchaseCommission = commissionRate * amountPaidForStock

stockSoldFor = sellingPrice * numShares

sellingCommission = stockSoldFor * commissionRate

totalCommission = sellingCommission + purchaseCommission

totalPaid = totalCommission + amountPaidForStock

totalReceived = stockSoldFor - totalPaid



print(f'Amount paid for stock ${amountPaidForStock}')

print(f'Commission paid on the purchase: ${purchaseCommission}')

print(f'Amount the stocks sold for: ${stockSoldFor}')

print(f'Commission paid on the sale: ${sellingCommission}')

print(f'Total commission paid"${totalCommission}')

print(f'Total ganed or lossed:${totalReceived}')

