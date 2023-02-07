old_price=[12,23,34,56,78,89,23,46]
rs=5
def add_price(no):
    return no+5
new_price=map(add_price,old_price)
new_price1=list(map(lambda n:n+rs,old_price))
print(list(new_price))
print(new_price1)