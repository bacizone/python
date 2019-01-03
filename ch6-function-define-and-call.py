def get_bark(weight):
    if weight > 20:
        return 'WOOOF WOOOF'
    else:
        return 'woof woof'

codies_bark = get_bark(40)
print("Codie's bark", codies_bark)