# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja az [indavideo](https://indavideo.hu/) oldalára automatikusan feltölti a számitógépen tárolt videó fájlokat. Python programozási nyelven íródott parancssoros alkalmazás, tehát nincs grafikus felület hozzá. Multiplatformos, tehát mind linuxon, mind windowson müködik. Nagy esélyel MacOS alatt is müködik, sajnos hardver hiányában ezt nem tudtam tesztelni.

---

## Telepítés
### Windows
A script használhatához a Windows Terminal nevű programot ajánlom. Ha nincsen még telepítve akkor [innen](https://apps.microsoft.com/detail/9N0DX20HK701?hl=neutral&gl=HU&ocid=pdpshare) tudod letölteni.

Terminálba ad ki az alábbi parancsokat\
Szükséges programok telepítése:
```bash
winget install python git.git
```
A script müködéséhez szükséges az alábbi python csomagok telepítése:
```bash
pip install bs4 requests
```
**Ezek után indítsd újra a számítógépedet**

Repozitori klonozása:
```bash
git clone https://github.com/Bence-3878/inda.git
```

### Linux
Nyisd meg a neked szimpatikus terminál emulátort\
Szükséges programok telepítése:
```bash
apt install git
```
A script müködéséhez szükséges az alábbi python csomagok telepítése:
```bash
pip install bs4 requests
```
## Használat

Az egész script használata az alábbi parancs:
Nyisd meg a terminált, és futtasd az alábbi parancsot:

```bash
python .\inda\inda.py upload [files]
```



## Pár tipp a terminál használatához
- az itt lévő parancsokat másold ki és illeszd be a terminálba
- minden legépelt sor vagy parancs után üss egy entert.
- a parancsokat egyenként kell kiadni
- a telepítésnél minden esetben üss [Y]es-t
- cd parancs segitségével lehet parancssorban navigálni a fájl rendszerben
- a tab billentyű ki egésziti a mappa neveket windows alatt linux alatt a parancsokat is

## Licens
Ez a program a GNU General Public License (GPL) 3. verziója alatt van licencelve.
További részletekért tekintsd meg a LICENSE fájlt.
