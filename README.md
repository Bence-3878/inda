# Automata indavideo feltőltő script
Ez a projekt ahogy a neve is mutatja az [indavideo](https://indavideo.hu/) oldalára automatikusan feltölti a számitógépen tárolt 
videó fájlokat. Python programozási nyelven íródott parancssoros alkalmazás, tehát nincs grafikus felület hozzá. 
Multiplatformos, tehát mind linuxon, mind windowson müködik. Nagy esélyel MacOS alatt is müködik, sajnos hardver 
hiányában ezt nem tudtam tesztelni.

---

## Telepítés
### Windows
A script használhatához a Windows Terminal nevű programot ajánlom. Ha nincsen még telepítve akkor 
[innen](https://apps.microsoft.com/detail/9N0DX20HK701?hl=neutral&gl=HU&ocid=pdpshare) tudod letölteni.

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
python inda.py upload [files]
```
A projekt könyvtárjában adható ki a fenti formában. A **[files]** helyére a feltölteni kivánt fájlokat kell felsoroni.\
Az első használat folyamán kérni forja az email cím jelszó párost, és a feltöltési beállítások beállítását. Az alapértelmezet beállítások 
az AnimeDrive szerkeszőinek készültek mindenki más számáza nem ajánlót a használata.

```bash
python inda.py config 
```

parancs segítségével bármikor modosítani lehet a configot

```bash
python inda.py reset
```

az egész programot alaphelyzetbe állítja

## Terminál használat alapok
Igyekszek általános lírást adni az összes támogatot platformra az esetleges különbségeket majd külön jelzem. Balról jobbra először a 
felhasználó amivel akituálisan be vagyunk jelentkezve utána az aktuális mappa elérési utja ahol jelenleg a fájl rendszerben tartozkodunk.
Mindig valamelyik mappa van megnyitva alapértelmezés szerint a terminál megnyilásakor a saját gyökér könyvtáradba kerülsz ahonnan a jól 
ismert mappák mint a képek, dokomentomuk, stb. nyilik. A script amenyiben mindent jól hajtotál végre a saját mabbád inda alkönyvtárába 
kerül. A elérési utban windows-on \\ míg Linuxon és MacOS alatt / tartalmaz. A perjel után lévő mappa egy almappája az előte lévő mappának.
A fájlrendszerben a **cd** parancs segitségével lehet az utána írt könyvtárba fog minket dobni. Az elérési út lehet abszulut és reatív az 
előbbi azt jelzi hogy az egész elérési utat az elejétől kezdve végig írjuk míg az utobbi azt hogy az aktuális mappához viszonitva adjuk 
meg az hová szertnék menni. A '..' a szülő könyvtárat jelőli. 
## Licens
Ez a program a GNU General Public License (GPL) 3. verziója alatt van licencelve.
További részletekért tekintsd meg a LICENSE fájlt.
