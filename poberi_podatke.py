import requests
import time

MAKSIMALNA_STRAN = 971
CAS_MED_ZAJEMANJEM = 0
ZNAMKA = "mercedes-benz"

for i in range(1, MAKSIMALNA_STRAN):
    time.sleep(CAS_MED_ZAJEMANJEM)
    url = f"https://www.truecar.com/used-cars-for-sale/listings/{ZNAMKA}/?page={i}"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        print(url)
        with open(f"cars_data_{ZNAMKA}/{ZNAMKA}_page_{i}.html", "w") as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")