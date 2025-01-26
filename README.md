# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja az [indavideo](https://indavideo.hu/) oldalára automatikusan feltölti a számitógépen tárolt 
videó fájlokat. Python programozási nyelven íródott parancssoros alkalmazás, ezáltal nincs grafikus felület hozzá. 
Multiplatformos, tehát mind linuxon, mind windowson müködik. Nagy esélyel MacOS alatt is müködik, sajnos hardver 
hiányában ezt nem tudtam tesztelni.

---

## Telepítés
### Windows
A script használhatához a Windows Terminal nevű programot ajánlom. Ha nincsen még telepítve akkor 
[innen](https://apps.microsoft.com/detail/9N0DX20HK701?hl=neutral&gl=HU&ocid=pdpshare) tudod letölteni.

Terminálba add ki az alábbi parancsokat:\
Szükséges programok telepítése:
```bash
winget install python git.git
```
A script müködéséhez szükséges az alábbi python csomagok telepítése:
```bash
pip install bs4 requests
```
**Ezek után indítsd újra a számítógépedet**

Repozitori klónozása:
```bash
git clone https://github.com/Bence-3878/inda.git
```

### Linux
Nyisd meg a neked szimpatikus terminál emulátort\
Szükséges programok telepítése:
```bash
apt update
apt install git
```
A script müködéséhez szükséges az alábbi python csomagok telepítése:
```bash
pip install bs4 requests
```
## Használat

A script legfontosabb és központi parancsa az alábbi:
```bash
python $HOME\inda\inda.py upload [files]
```
A projekt könyvtárában adható ki a fenti formában. A **[files]** helyére a feltölteni kivánt fájlokat kell felsorolni.\
Az első használat folyamán kérni fogja az email cím-jelszó párost, és a feltöltési beállításokat. Az alapértelmezett beállítások 
az AnimeDrive szerkesztőinek készültek, mindenki más számára nem ajánlott a használata.

```bash
python $HOME\inda\inda.py config 
```

parancs segítségével bármikor modosítani lehet a config-ot

```bash
python $HOME\inda\inda.py reset
```
az egész programot alaphelyzetbe állítja


## Terminál használat alapok
mappa elérési útja szerepel, ahol most is vagyunk. Míg linuxon és Mac-en először balról jobbra haladva a _felhasználónév@gépnév_ látszik,
  amivel akituálisan be vagyunk jelentkezve, és végül a mappa elérési útja, ahol jelenleg a fájl rendszerben tartózkodunk.
  Mindig valamelyik mappa van megnyitva alapértelmezett szerint. A terminál megnyitásakor a saját gyökér könyvtáradba kerülsz, ahonnan a jól 
  ismert mappák, mint a képek, dokumentummok, stb. nyílik. A sáját mappa elérési útját a `$HOME` környezeti változó is tertalmazza. 
  A script, amennyiben mindent jól hajttotál végre a saját mappád inda alkönyvtárába 
  kerül. Az elérési útban windows-on \\ jelet, míg Linuxon és MacOS alatt / jelet tartalmaz.\
  A fájlrendszerben a `cd` parancs segitségével lehet nagigálni. 
```bash
cd [elérési út]
```
  Az elérési út lehet abszólut és relatív. Az 
  előbbi azt jelenti, hogy az egész elérési utat az elejétől kezdve végig írjuk, míg az utóbbi azt, hogy az aktuális mappához víszonyitva adjuk 
  meg azt, hogy hová szertnénk menni. A `..` a szülő könyvtárat jelöli. 

## Pár tipp a terminál használatához
- az itt lévő parancsokat másold ki és illeszd be a terminálba
- minden legépelt sor vagy parancs után üss egy entert.
- a parancsokat egyenként kell kiadni
- a telepítésnél minden esetben üss [Y]es-t
- a tab billentyű ki egésziti a mappa neveket windows alatt linux alatt a parancsokat is
  Igyekszek általános leírást adni az összes támogatott platformra, az esetleges különbségeket majd külön jelzem. Windows-on csak az aktuális
## Licens
  Ez a program a GNU General Public License (GPL) 3. verziója alatt van licencelve.
További részletekért tekintsd meg a LICENSE fájlt.
