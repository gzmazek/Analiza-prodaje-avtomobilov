import re
import json
import csv

#######################################

ZNAMKA_STRANI = [("mercedes-benz", 971), ("bmw", 918), ("audi", 508)]
ZNAMKA_STRANI_POSKUS = [("mercedes-benz", 90), ("bmw", 91), ("audi", 50)]

pravilnih = 0

#######################################

vzorec_bloka = re.compile(
    r'<li\sclass="mt(?P<blok>.+?)'
    r'</div>\s*</li>',
    flags=re.DOTALL
)

vzorec_oglasa = re.compile(
    r'<a\shref="/used-cars-for-sale/listing/(?P<primary>.*?)/".*'
    r'data-test="vehicleCardPricingBlockPrice">(?P<price>.*?)</div>.*'
    r'</circle>\s*</svg>(?P<miles>.*?)<!--\s-->\smiles</div>.*'
    r'</path></svg>(?P<city>.*?)<!--\s-->,\s<!--\s-->(?P<state>.*?)</div><div\sclass="vehicle-card-location.*'
    r'</svg>(?P<exterior>.*?)<!--\s-->\sexterior.*'
    r'-->(?P<interior>.*?)<!--\s-->\sinterior</div></div><div.*'
    r'</path></svg>(?P<accidents>.*?)\saccidents?,\s(?P<owners>.*?)\sOwners?,\s(?P<use>.*?)\suse</div>.*'
    r'ill-rule="evenodd"></path></svg>(?P<podatki>.*?)</div><div\sclass="vehicle-card.*',
    flags=re.DOTALL
)

#####################################################################################################################
########################################   FUNKCIJE ZA ČIŠČENJE PODATKOV     ########################################
#####################################################################################################################

def vzorec_primary(znamka):
    return re.compile(
        fr'(?P<VIN>.+)/(?P<year>\d{{4}})-{znamka}-(?P<model>.*)',
        flags=re.DOTALL
    )

def predelaj_primary(primary, znamka):
    return vzorec_primary(znamka).search(primary).groupdict()

def predelaj_podatki_motor(podatki):
    """Funkcija vzame niz podatkov in vrne ločene podatke, porabo vrne 0, če podatka ni"""
    if "MPG" not in podatki:
        podatki = "MPG: 0-0, " + podatki
    slovar_podatki = re.search(r'MPG:\s(?P<MPG_city>\d+)-(?P<MPG_highway>\d+),\sEngine:\s(?P<engine>.*),\sTransmission:\s(?P<transmission>.*),\s(?P<drive_type>.*)', podatki).groupdict()
    return slovar_podatki
        


#####################################################################################################################
#####################################################################################################################

def predelaj_podatke_oglasa(oglas, znamka):
    try: # Ker so nekateri oglasi nepopolni (brez porabe, ki je knjična za analizo), so filtrirani le oglasi, ki vsebujejo potrebne informacije) - nepravilnih je približno 42%
        avto = vzorec_oglasa.search(oglas.group(0)).groupdict()
        osnovni_podatki = predelaj_primary(avto.pop("primary"), znamka)
        avto["VIN"] = osnovni_podatki["VIN"]
        avto["year"] = int(osnovni_podatki["year"])
        avto["model"] = osnovni_podatki["model"]
        avto["price"] = int(avto["price"].lstrip("$").replace(",", ""))
        avto["miles"] = int(avto["miles"].replace(",", ""))
        avto["accidents"] = int(avto["accidents"].replace("No", "0"))
        avto["owners"] = int(avto["owners"])
        motorni = predelaj_podatki_motor(avto.pop("podatki"))
        avto["MPG_city"] = motorni["MPG_city"]
        avto["MPG_highway"] = motorni["MPG_highway"]
        avto["engine"] = motorni["engine"]
        avto["transmission"] = motorni["transmission"]
        avto["drive_type"] = motorni["drive_type"]

        #print(avto["podatki"])
        global pravilnih 
        pravilnih += 1
        return avto
    except: 
        pass

#####################################################################################################################
#####################################################################################################################

cars = []

for ZNAMKA, STRANI in ZNAMKA_STRANI_POSKUS:
    for i in range(1, STRANI):
        with open(f"cars_data_{ZNAMKA}/{ZNAMKA}_page_{i}.html") as f:
            vsebina = f.read()
        for blok in vzorec_bloka.finditer(vsebina):
            car = predelaj_podatke_oglasa(blok, ZNAMKA)
            if car:
                cars.append(car)

with open("cars.json", "w") as f:
    json.dump(cars, f, ensure_ascii=False, indent=4)

# with open("cars.csv", "w") as f:
#    pisatelj = csv.DictWriter(f, fieldnames=[])
#    pisatelj.writeheader()
#    for car in cars:
#        pisatelj.writerow(car)


# halo = "mercesed-benz"
# print(re.search(fr'(?P<VIN>.+)/(?P<year>\d{{4}})-{halo}-(?P<model>.*)', 'WA1ANAFYXK2079056/2019-audi-q5').groupdict()["year"])
