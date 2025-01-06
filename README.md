# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja az [indavideo](https://indavideo.hu/) oldalára automatikusan feltölti a számitógépen tárolt videó fájlokat. Pythonban íródott parancssoros interfészt használ. Multiplatformos, tehát mind linuxon, mind windowson müködik.

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

ez után töltsd le fájlt a repoból, vagy add ki a következő parancsot (ha van git a számítógépen)
> git clone https://github.com/Bence-3878/inda.git
## Használat

### 1. Be kell lépni az inda fiókodba

> python inda.py login

Ez után parancssorban megkell adni a bejelentkezési adatokat felhasználónév jelszó. A számitógepen van csak tárolva.

### 2. videó feltöltése

> python inda.py upload [files]

a végére a feltölteni kivánt fájlokat kell írni
