# Hackaton 2023 

## A programról:
Minden feladatban követtem a leírást, viszont a Snake-t és a harmadik feladatot kibővítettem. 

Az első feladatban megoldottam, hogy a program a konzolba jelenítse meg kijelzőjét, és mindíg törölje az előzőt, így könyebb használni. Extra funkciók:
- almák, random jelennek meg, és növelik a kígyó hosszát. Tudom, hogy az ikon eltolja a konzolt, de ez egy feature, azért, hogy könyebben észre lehessen venni, hogy jó sorban vagyunk.
- Irányátás: fel, le, lalra, lobbra, meguntam
- Gyorsgombok: bal, jobb, fel, le, enter, x
- Az enter parancs annyit tesz, hogy üres parancsot küldünk, ilyenkor megismétli az előző elküldött parancsot, a gyorsabb haladás érdekében.
- Pontrendszer
- Ha magadba vagy a falnak mész, meghalsz

A harmadik feladat tud magyarul és angolul is pizzát rendelni, és megerősítés után "leadja a rendelést". Egy gpt-3.5-turbo motorral, llma-index-el, és langchainel, egy lokális nyelvi model kollaborál a netes gpt-3.5-turbo api-val, hogy elkészüljön a rendelés.
- A `pizzabot\trainData\PizzaChat.txt` fájlban látható a lokális tanítási adat.
- A fájt elég futtatni, és beszélgetnmi vele, a bot tudni fogja, mikor van vége a rendelésnek, és le is adja utánna. (Kiírja, hogy rendelés leadva, kicsit drága lenne a Volt API-val összekötni tesztelés céljából :D)
- Jegyzetet ír arról, hogy mit kért a felhasználó. Ezt a videüban ugyan nem printelem ki, de késöbbi fejlesztés során haszonos lehet.
### Szükséges programok:
- python 3.11.2
  - pip packagek:
  - openai==0.27.7
  - langchain==0.0.183
  - llama_index==0.6.13

### Javasolt használati mód:

Python Virtual Enviroment (venv) használata.
A venv segítségével ugyanazt a futtató környezetet lehet használni több számító gépen is, így nem kell minden gépen külön telepíteni a szükséges packageket. Ráadásul előfordul, hogy valaki egy másik verzióju python packeget használ, és így a verseny során nem tudja futtatni a programját.
Ennek használatához a következőket kell tenni:

## Ha meglévő virtuális környezetet akar használni:
1. Nyisson egy terminált
2. `cd <projekt mappa elérési útja, az a hely ahol ez a readme van>`
3. Nyissa meg a megfelelő munkaterület aktiválási scriptet, rendszere alapján:
   1. Windows: PowerShell: `Hackaton2023\Scripts\Activate.ps1`
   2. Windows: CMD: `Hackaton2023\Scripts\activate.bat`
   3. Linux / MAC: `source Hackaton2023/bin/activate`
4. Innentől használhatja úgy a megnyitott terminált, mint egy normál terminált, ahol a python parancs a venv-ben lévő python interpretert fogja használni, és a pip parancs a venv-ben lévő pip-et fogja használni. Elméletileg nem kell már semmit se telepíteni, de a biztonság kedvéért futtassa le a következő parancsot:
   1. `pip install -r requirements.txt
## Ha új virtuális környezetet akar használni:
1. Nyisson egy terminált
2. `cd <projekt mappa elérési útja, az a hely ahol ez a readme van>`
3. Hozzon létre egy munkamenetet a következő paranccsal: `python -m venv <egyedi név>`
4. Nyissa meg a megfelelő munkaterület aktiválási scriptet, rendszere alapján:
   1. Windows: PowerShell: `<egyedi név>\Scripts\Activate.ps1`
   2. Windows: CMD: `<egyedi név>\Scripts\activate.bat`
   3. Linux / MAC: `source <egyedi név>/bin/activate`
5. Innentől használhatja úgy a megnyitott terminált, mint egy normál terminált, ahol a python parancs a venv-ben lévő python interpretert fogja használni, és a pip parancs a venv-ben lévő pip-et fogja használni.
6. **Telepítse fel a csomagokat**
   1. `pip install -r requirements.txt
`
    

Az OpenAI api kulcsot a következő helyre kell bemásolni:
`pizzabot/pizzabot.py` 12.sor
```py
    os.environ["OPENAI_API_KEY"] = "IDE-KELL-A-KULCSOT" # ide kell majd az emailban kapott kulcsot bemásolni
```

Amennyiben nem sikerült se virtual enviromentel, se máshogy feltelepíteni a csomagokat, akkor íme egy videó arról, hogy kell működnie: a programnak:
https://youtu.be/gEa2xLy4xS0
A videóban lévő kódban szereplú API kulcs már nem érvényes, újra generáltam. Emellett a felvétel óta beleraktam még egy printet, amely kiírja a bot által készített jegyzeteket, melyeket továbbíthatok a futárnak. Ez az egy különbözik a jelenlegi kódban lévőtől.

Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved