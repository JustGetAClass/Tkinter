def add(*args):
    total = 0
    for n in args:         # simpler way -->  return sum(args)
        total += n
    return total           # args uses tuples


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)                                 # kwargs uses dictionary


calculate(2, add=5, mult=10)


# creating default values or the **kwargs
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make", 'Toyota')
