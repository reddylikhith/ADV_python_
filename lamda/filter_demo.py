l=[5,23,45,67,89,12]
def demo_fun(n):
    if n>=10:
        return True
    else:
        return False
data=list(filter(demo_fun,l))
print(data)