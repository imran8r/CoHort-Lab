class Playtime:
    def __init__(self, a, b, c):  # Use __init__ instead of _init_
        self.a = a
        self.b = b
        self.c = c

point = Playtime(1, 2, 3)
print(point.a)  # Access the 'a' attribute through the instance
