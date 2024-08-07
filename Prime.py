def primzahl(zahl):
    if zahl==2:
        return True 
    if zahl/2 - int(zahl/2) ==0:
        # print(f"Die Zahl {zahl} ist gerade. Daher keine Primzahl.")
        return False
    if zahl/3 - int(zahl/3) ==0:
        return False
    if zahl > 5:
        if zahl/5 - int(zahl/5) ==0:
            return False
    return True 


for zahl in range(2,41):
    if primzahl(zahl):
        print(zahl)

print('ende')
