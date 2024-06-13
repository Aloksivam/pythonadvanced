# li = [{'name': 'coffee', 'price': 2.5}, {'name': 'soup', 'price': 4.5}, {'name': 'espresso', 'price': 1.99}]
# name = [i['name'] for i in li]
# print(*lis)
# order = [{'name': 'coffee', 'price': 2.5}, {'name': 'soup', 'price': 4.5}, {'name': 'espresso', 'price': 1.99}]
subtotal = 0.0
for i in order:
    if(i['name']=='coffee'):
        subtotal+=2.5
    elif(i['name']=='espresso'):
        subtotal+=1.99
    elif(i['name']=='cake'):
        subtotal+=2.79
    elif(i['name']=='soup'):
        subtotal+=4.50
    else:
        subtotal+=4.99
print(subtotal)