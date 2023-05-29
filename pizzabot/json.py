## A JSON kiszedésére volt egy teszt.

#Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved
import json, re

def JSONGetter(text):
    global Gstatus
    first = text.index('{')
    last = text.index('}')
    jsonText = text[first:last+1]
    jsonText = re.sub(r'//.*', '', jsonText)
    pyData = json.loads(jsonText)
    Gstatus = pyData['status']
    print(pyData['response'], "\n---\n")
    return pyData
response = 'Your reply:\n{\n  "response": "A sajtos pizzák, nagy méretben, 2000 Ft-ba kerülnek. Az őszibaracklé 500 Ft-ba kerül, és a 5 kóla 2500 Ft-ba kerül. Összesen 6500 Ft-ba fog kerülni.", // response in user choosen primary language\n  "status": "end",\n  "notes": "cheese, large, peach juice, cheese, large, olives, peppers, 5 cokes" //notes in english\n}'

JSONGetter(response)
#Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved