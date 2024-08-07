def primzahl(zahl):
    if zahl / 2 == int(zahl/2):
        return False
    return True

for zahl in range(2, 11):
    if primzahl(zahl):
        print(zahl)

print('ende')
