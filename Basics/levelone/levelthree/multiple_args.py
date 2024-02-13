def subtractme(*args):
    if len(args) != 2:
        raise ValueError("Function only accepts 2 values")
    else:
        total = 100
        for i in args:
            total = total - i
        return total

# myVal = addme(3,5)
print(subtractme(20,30,50))