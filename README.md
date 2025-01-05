# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja. Az [indavideo](https://indavideo.hu/) oldalára automatikusan feltőlt a számitógépen tárolt videó fájlokat. Pythonban írodot parancssoros interfészt használ. Multiplatformos mind linuxon mind windowson müködik.

---
## Telepítés
### windows
Terminálba ki kell adni az alábbi parancsot:
> winget install python

vagy letölteni az alábbi [weboldaloról](https://www.python.org/downloads/) az aktuális verziót.

> pip install bs4
> 
> pip install requests

szükséges python csomagok telepítése

**A rendszer ujra inditása szükséges**
## Használat

### 1. Be kell lépni az inda fiókodba

> python inda.py login

Ez után parancssorban megkell adni a bejelentkezési adatokat felhasználónév jelszó. A számitógepen van csak tárolva.

### 2. videó feltöltése

> python inda.py upload [files]

a végére a feltölteni kivánt fájlokat kell írni
