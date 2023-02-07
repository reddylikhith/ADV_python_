def outer():
    print("hello from outer function")
    def inner():
        print("inner functiom")
    return inner
d=outer()
d()