def greet(fx):
    def mfx(*args, **kwargs):
        print("Namaste")
        fx(*args, **kwargs)
        print("Thanks")
    return mfx


@greet
def hello():
    print("Hello World")


@greet
def add(a, b):
    print(a + b)


# greet(hello())
# hello()
add(1, 2)
