print("Retail Prices")
print('1. Product1:  12.98')
print('2. Product2:  44.50')
print('3. Product3:  99.98')
print('4. Product5:  126.87')
items={
    'Product1': 12.98,
    'Product2': 44.50,
    'Product3': 99.98,
    'Product4': 74.49,
    'Product5': 126.87
}
want="yes"
want=str(input("Do you want cheap:"))
if want=="yes" :
     print(min(zip(items.values(),items.keys())))
elif want=="n" or want=="no":
     print(max(zip(items.values(),items.keys())))
else:
     print(items)