def decor(func):
    def inner(name):
        if name=="hcl":
            print("hello hcl func")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name)
wish("hcl")
wish("wipro")