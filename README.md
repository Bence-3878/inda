# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja az [indavideo](https://indavideo.hu/) oldalára automatikusan feltölti a számitógépen tárolt videó fájlokat. Python programozási nyelven íródott parancssoros alkalmazás, tehát nincs grafikus felület hozzá. Multiplatformos, tehát mind linuxon, mind windowson müködik. Nagy esélyel MecOS alatt is müködik, sajnos hardver hiányában ezt nem tudtam tesztelni.

---
## Telepítés
### windows
A script használhatához a Windows Terminal nevű programot ajánlom. Ha nincsen még telepítve akkor [innen](https://apps.microsoft.com/detail/9N0DX20HK701?hl=neutral&gl=HU&ocid=pdpshare) tudod letölteni.

Terminálba ki kell adni az alábbi parancsot:
> winget install python

megjegyzés: a telepítés során felmerülő választási lehetőségeknél mindig írd be a yes-t.
Minden legépelt sor vagy parancs után üss egy entert.

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
