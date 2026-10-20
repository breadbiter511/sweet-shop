import numpy as np
print("WELCOME TO MY SWEET SHOP!")
items = np.array(["twix","haribo","mars","cadbury","milky-way","snickers","milka","trolli","reeces","sour-patch-kids"])
price = np.array([90,200,70,120,80,70,220,100,150,250])
stock = np.array([10,21,30,24,14,15,12,27,2,40])
print(type(items))
print(items)
print(price)
print("there are",len(items),"different sweets for sale")
print("the number of items are",items.size)#len and size tell us how many items are in an array
individual_stock_value = price * stock
print(individual_stock_value)
total_stock_value = np.sum(individual_stock_value)#sum adds all the values to calculate the sum(not possible with lists)
print("the total stock value is ",total_stock_value)
for i in range(len(items)):
    print(items[i],individual_stock_value[i])
print("++++++++++++++++++++++++")
print("ITEM    PRICE    STOCK")
for i in range(len(items)):
    print(items[i]," ",price[i]," ",stock[i])
average_price = np.sum(price) / 10# or np.mean
average_price2 = np.mean(price)
print("the average price is ",average_price)
print(average_price2)
median_price = np.median(price)
print("the median price is ",median_price)
minimum_price = np.min(price)
print("the minimum price is ",minimum_price)
maximum_price = np.max(price)
print("the maximum price is ",maximum_price)