# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja az [indavideo](https://indavideo.hu/) oldalára automatikusan feltölti a számitógépen tárolt videó fájlokat. Python programozási nyelven íródott parancssoros alkalmazás, tehát nincs grafikus felület hozzá. Multiplatformos, tehát mind linuxon, mind windowson müködik. Nagy esélyel MecOS alatt is müködik, sajnos hardver hiányában ezt nem tudtam tesztelni.

---
## Pár tipp a terminál használatához
- az itt lévő parancsokat másold ki és illeszd be a terminálba
- minden legépelt sor vagy parancs után üss egy entert.
- a parancsokat egyenként kell kiadni
- a telepítésnél minden esetben üss [Y]es-t
- cd parancs segitségével lehet parancssorban navikálni a fájl rendszerben
- a tab billentyű ki egésziti a mappa neveket windows alatt linux alatt a parancsokat is

## Telepítés
### windows
A script használhatához a Windows Terminal nevű programot ajánlom. Ha nincsen még telepítve akkor [innen](https://apps.microsoft.com/detail/9N0DX20HK701?hl=neutral&gl=HU&ocid=pdpshare) tudod letölteni.

Terminálba ki kell adni az alábbi parancsot:
> winget install python git.git

A script müködéséhez szükséges az alábbi python csomagok telepítése:
> pip install bs4
> 
> pip install requests


**Ezek után indítsd újra a számítógépedet**



repozitori klonozása
> git clone https://github.com/Bence-3878/inda.git

## Használat

az egész script használata az alábbi parancs
a terminál megnyitásakor a

> python /path/to/file/inda.py upload [files]


