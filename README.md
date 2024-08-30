# Mein erstes Python programm

[![GitHub release](https://img.shields.io/github/release/LiBeKra/Python24.svg)](https://GitHub.com/LiBeKra/Python24/releases/)
[![MIT license](https://img.shields.io/github/license/LiBeKra/Python24)](https://LiBeKra.mit-license.org/)


## Primzahlen berechnen

Wir fangen einfach an:

``` py
def primzahl(zahl):
  return True

for zahl in range(2,100):
  if primzahl(zahl):
    print(zahl)
```

# Update

``` py
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
```

## Start 6. August 2024

Dies ist der Erste Absatz mehr kommt später.

### Projekt von Matthias Kreier und LiBeKra.
